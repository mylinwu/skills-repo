#!/usr/bin/env python3
"""
Linux DO RSS 智能摘要脚本
功能：获取 RSS → 提取字段（去 HTML）→ 调用 AI 分类摘要并按重要度排序

用法：
  python linuxdo_rss_digest.py                          # 默认：处理所有源，最近24h，过滤低价值分类
  python linuxdo_rss_digest.py --source latest          # 只处理最新话题
  python linuxdo_rss_digest.py --source top             # 只处理热门话题
  python linuxdo_rss_digest.py --hours 6                # 最近6小时
  python linuxdo_rss_digest.py --no-filter             # 不过滤低价值分类
  python linuxdo_rss_digest.py --limit 50              # 只看最新50条
  python linuxdo_rss_digest.py --categories 前沿快讯,开发调优  # 只看指定分类
  python linuxdo_rss_digest.py --output-only            # 只输出 JSON，不调用 AI
"""

import re
import json
import os
import sys
import argparse
from datetime import datetime, timezone, timedelta
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET
from html import unescape

# ──────────────────────────────────────────────
# 配置区
# ──────────────────────────────────────────────

# RSS 源配置：每个源包含 URL 和 source_type（用于 AI 分析时区分"最新"或"热门"）
RSS_SOURCES = {
    "最新话题": {
        "url": "https://linuxdorss.longpink.com/latest.xml",
        "source_type": "latest",
    },
    "热门话题": {
        "url": "https://linuxdorss.longpink.com/top.xml",
        "source_type": "top",
    },
}

# 脚本所在目录（输出文件默认保存在这里）
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 默认过滤掉的低价值分类（可在命令行用 --no-filter 取消过滤）
DEFAULT_FILTERED_CATEGORIES = {
    "搞七捻三",   # 社区闲聊，量大低价值
    "读书成诗",   # 诗词创作
    "虫洞广场",   # 闲聊
}

# AI 配置（从环境变量读取，避免硬编码）
AI_API_URL = os.getenv("AI_API_URL", "https://api.openai.com/v1/chat/completions")
AI_API_KEY = os.getenv("AI_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "gpt-4o-mini")
AI_MAX_TOKENS = int(os.getenv("AI_MAX_TOKENS", "3000"))

# 如果 AI_API_KEY 为空则跳过 AI 分析，只输出 JSON
SKIP_AI = not AI_API_KEY

# ──────────────────────────────────────────────
# RSS 解析
# ──────────────────────────────────────────────

def fetch_rss(url: str, timeout: int = 60) -> str:
    """获取 RSS XML 内容（含 SSL 容错 + 重试）"""
    import ssl
    from urllib.error import URLError

    headers = {"User-Agent": "Mozilla/5.0 (Linux DO RSS Reader)"}

    # 尝试多次，逐步放宽 SSL 要求
    for attempt in range(3):
        try:
            # 第一次及以后：尝试普通请求
            req = Request(url, headers=headers)
            ctx = None
            if attempt >= 1:
                # 重试：忽略证书验证
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
            with urlopen(req, timeout=timeout, context=ctx) as resp:
                return resp.read().decode("utf-8")
        except ssl.SSLError:
            if attempt == 2:
                raise
            print(f"   SSL 错误，重试中 ({attempt + 2}/3)...")
            import time; time.sleep(2)
        except URLError as e:
            if "SSL" in str(e) and attempt < 2:
                print(f"   URL/SSL 错误，重试中 ({attempt + 2}/3)...")
                import time; time.sleep(2)
                continue
            raise


def strip_html(html: str) -> str:
    """去除 HTML 标签，保留纯文本"""
    if not html:
        return ""
    # 移除 <script> 和 <style> 标签内容
    html = re.sub(r"<(script|style)[^>]*>.*?</(script|style)>", "", html, flags=re.DOTALL | re.IGNORECASE)
    # 将 <br>, <p>, </p>, </div> 等替换为换行
    html = re.sub(r"<br\s*/?>", "\n", html, flags=re.IGNORECASE)
    html = re.sub(r"</(p|div|li|tr|h[1-6])>", "\n", html, flags=re.IGNORECASE)
    # 移除所有 HTML 标签
    html = re.sub(r"<[^>]+>", "", html)
    # HTML 实体解码
    html = unescape(html)
    # 合并多余空行
    html = re.sub(r"\n{3,}", "\n\n", html)
    # 去除首尾空白
    return html.strip()


def parse_rss(xml_content: str, source_type: str = "latest") -> list[dict]:
    """解析 RSS XML，提取 item 列表
    
    Args:
        xml_content: RSS XML 内容
        source_type: 源类型标识，用于区分"最新"或"热门"
    """
    root = ET.fromstring(xml_content)
    items = []
    ns = {
        "dc": "http://purl.org/dc/elements/1.1/",
        "atom": "http://www.w3.org/2005/Atom",
    }

    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        category = (item.findtext("category") or "").strip()
        description = (item.findtext("description") or "").strip()
        link = (item.findtext("link") or "").strip()
        pub_date = (item.findtext("pubDate") or "").strip()
        creator = (item.findtext("dc:creator", namespaces=ns) or "").strip()

        items.append({
            "title": title,
            "category": category,
            "description_text": strip_html(description),
            "link": link,
            "pubDate": pub_date,
            "creator": creator,
            "source_type": source_type,  # 添加源类型标识
        })

    return items


# ──────────────────────────────────────────────
# AI 分析
# ──────────────────────────────────────────────

def build_ai_prompt(items: list[dict]) -> str:
    """构建发给 AI 的提示词"""
    json_input = json.dumps(items, ensure_ascii=False, indent=2)

    return f"""你是一个信息筛选助手，专门帮助用户从论坛 RSS 中快速发现有价值的信息。

下面是 Linux DO 论坛的帖子列表（JSON 格式，已去除 HTML 标签）：
```json
{json_input}
```

**重要说明**：
- 每个帖子有 `source_type` 字段，值为 "latest" 或 "top"
- `source_type: "latest"` 表示**最新话题/最新资讯**，即最近发布的内容
- `source_type: "top"` 表示**热门话题/热门资讯**，即社区热门讨论的内容
- 在输出时，请在分组名称中体现这些帖子的来源特征（最新 or 热门）

请按以下要求处理：

1. **分类**：将帖子按主题分为 3-5 个分组，例如：
   - 🔬 科技前沿（新技术、研究进展、产品发布）
   - 💻 开发技术（编程、工具、部署相关）
   - 🤖 AI 相关（AI 产品、模型、应用）
   - 📦 开源项目（开源工具、框架发布）
   - 🎁 福利羊毛（免费资源、优惠信息）

2. **重要度排序**：在每个分组内，按信息价值从高到低排序。
   重要度评估标准：
   - 【高】具有实用价值、可操作、行业重要动态
   - 【中】有趣但非紧急、一般性讨论
   - 【低】纯闲聊、表情包、无意义内容

3. **输出格式**（严格按照以下格式，不要添加分类和链接字段）：
============= 分组名称 =============
【推荐等级】标题
摘要内容（2-3句话，简洁概括核心信息）

【推荐等级】标题
摘要内容

============= 分组名称 =============
【推荐等级】标题
摘要内容

要求：
- 分组名称用 "=" 包裹，格式：============= 分组名称 =============
- 每个条目只有：推荐等级（【高】/【中】/【低】）+ 标题 + 摘要
- 不要输出分类、链接、作者等额外字段
- 摘要要简洁（2-3句话），帮助用户快速判断是否值得点开原文
- 如果某个分组内容较少（少于3条），可以不输出该分组
"""


def call_ai(prompt: str) -> str:
    """调用 AI API（OpenAI 兼容格式）"""
    import urllib.request
    import json as json_lib

    payload = {
        "model": AI_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": AI_MAX_TOKENS,
        "temperature": 0.3,
    }

    data = json_lib.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        AI_API_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AI_API_KEY}",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json_lib.loads(resp.read().decode("utf-8"))

    return result["choices"][0]["message"]["content"]


# ──────────────────────────────────────────────
# 主流程
# ──────────────────────────────────────────────

def filter_items(
    items: list[dict],
    hours: int = 24,
    filtered_categories: set = None,
    allowed_categories: list = None,
    limit: int = None,
) -> list[dict]:
    """按时间、分类过滤帖子"""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)

    result = []
    for it in items:
        # 时间过滤
        try:
            dt = datetime.strptime(it["pubDate"], "%a, %d %b %Y %H:%M:%S %z").astimezone(timezone.utc)
            if dt <= cutoff:
                continue
        except Exception:
            pass  # 日期解析失败则保留

        # 分类过滤
        cat = it.get("category", "")
        if filtered_categories and cat in filtered_categories:
            continue
        if allowed_categories and cat not in allowed_categories:
            continue

        result.append(it)

    # 按发布时间排序（新的在前）
    def parse_date(it):
        try:
            return datetime.strptime(it["pubDate"], "%a, %d %b %Y %H:%M:%S %z")
        except Exception:
            return datetime.min.replace(tzinfo=timezone.utc)

    result.sort(key=parse_date, reverse=True)

    if limit:
        result = result[:limit]

    return result


def main():
    parser = argparse.ArgumentParser(description="Linux DO RSS 智能摘要脚本")
    parser.add_argument("--hours", type=int, default=24, help="抓取最近 N 小时的帖子（默认 24）")
    parser.add_argument("--no-filter", action="store_true", help="不过滤低价值分类")
    parser.add_argument("--categories", type=str, default=None, help="只看指定分类，逗号分隔，如：前沿快讯,开发调优")
    parser.add_argument("--limit", type=int, default=None, help="最多处理 N 条（默认全部）")
    parser.add_argument("--output-only", action="store_true", help="只输出 JSON，不调用 AI")
    parser.add_argument("--source", type=str, default="all", help="选择 RSS 源：latest(最新话题), top(热门话题), all（默认 all）")
    args = parser.parse_args()

    # 源类型映射：支持中英文
    source_alias = {
        "latest": "最新话题",
        "top": "热门话题",
        "all": "all",
    }
    
    # 确定要处理的 RSS 源
    source_key = source_alias.get(args.source, args.source)
    
    if source_key == "all":
        sources_to_process = RSS_SOURCES.items()
    elif source_key in RSS_SOURCES:
        sources_to_process = [(source_key, RSS_SOURCES[source_key])]
    else:
        print(f"❌ 错误：不支持的源类型 '{args.source}'")
        print(f"   支持的源类型：latest(最新话题), top(热门话题), all")
        sys.exit(1)

    all_items = []
    
    # 循环处理每个 RSS 源
    for source_name, source_config in sources_to_process:
        source_url = source_config["url"]
        source_type = source_config["source_type"]
        
        print(f"\n📡 正在获取 RSS 源: {source_name} ({source_url})")
        try:
            xml_content = fetch_rss(source_url)
            print(f"✅ RSS 获取成功，大小: {len(xml_content)} 字符")
            
            items = parse_rss(xml_content, source_type=source_type)
            print(f"✅ 解析完成，共 {len(items)} 条帖子")
            all_items.extend(items)
        except Exception as e:
            print(f"❌ 获取 {source_name} 失败: {e}")
            continue

    if not all_items:
        print("⚠️  所有 RSS 源都获取失败，退出")
        return

    print(f"\n📊 总计获取帖子数: {len(all_items)}")

    # 过滤
    filtered_cats = set() if args.no_filter else DEFAULT_FILTERED_CATEGORIES
    allowed_cats = args.categories.split(",") if args.categories else None
    filtered = filter_items(
        all_items,
        hours=args.hours,
        filtered_categories=filtered_cats,
        allowed_categories=allowed_cats,
        limit=args.limit,
    )
    print(f"✅ 过滤后剩余: {len(filtered)} 条（时间: 最近 {args.hours}h，分类过滤: {'否' if args.no_filter else '是'}）")

    if not filtered:
        print("⚠️  没有符合条件的帖子")
        return

    # 保存过滤后的 JSON
    output_json = os.path.join(SCRIPT_DIR, "linuxdo_rss_filtered.json")
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(filtered, f, ensure_ascii=False, indent=2)
    print(f"📄 过滤后数据已保存至: {output_json}")

    if args.output_only:
        print("✅ 仅输出 JSON，跳过 AI 分析")
        return

    if SKIP_AI:
        print("\n⚠️  未配置 AI_API_KEY 环境变量，跳过 AI 分析。")
        print(f"   请设置环境变量后重新运行：")
        print(f"   export AI_API_KEY=your_key")
        print(f"   export AI_API_URL=https://your-api-endpoint/v1/chat/completions")
        print(f"   export AI_MODEL=gpt-4o-mini  # 可选")
        print(f"   或直接在此脚本同目录运行：python linuxdo_rss_digest.py --output-only")
        return

    print(f"\n🤖 正在调用 AI 分析（模型: {AI_MODEL}）...")
    prompt = build_ai_prompt(filtered)
    result = call_ai(prompt)

    output_md = os.path.join(SCRIPT_DIR, "linuxdo_rss_digest.md")
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"✅ AI 摘要已保存至: {output_md}")
    print("\n" + "=" * 60)
    print(result)
    print("=" * 60)


if __name__ == "__main__":
    main()
