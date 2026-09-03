---
name: linuxdo-rss-digest
description: >
  Linux DO 论坛 RSS 智能摘要技能。当用户要求总结 Linux DO 最新话题、最新新闻、要闻、论坛动态，
  或需要快速浏览 Linux DO 论坛高价值内容时触发。自动获取 RSS，过滤低价值内容，调用 AI 分类摘要并按重要度排序输出。
agent_created: true
---

# Linux DO RSS 智能摘要技能

## 功能概述

自动获取 Linux DO 论坛 RSS feed（支持**最新话题**和**热门话题**两个源），提取帖子标题、分类和描述（去除 HTML 标签），过滤低价值分类（如"搞七捻三"），调用 AI 对剩余内容进行智能分类和摘要，按重要度排序输出。

**支持的两个 RSS 源**：
- **最新话题** (`latest.xml`)：最近发布的内容，归类为"最新话题/最新资讯"
- **热门话题** (`top.xml`)：社区热门讨论的内容，归类为"热门话题/热门资讯"

## 触发条件

当用户提出以下类型请求时，使用此技能：
- "总结 Linux DO 最新话题/最新资讯"
- "Linux DO 有什么新动态/热门讨论"
- "帮我看看论坛最近有什么重要内容"
- "Linux DO 要闻/最新新闻/热门资讯"
- "总结 Linux DO 热门话题"
- 任何涉及 Linux DO 论坛内容摘要的请求

## 执行流程

### 1. 检查 Python 环境

确认 Python 可用（优先使用 managed Python）：
- Windows: `C:\Users\daren_admin\.workbuddy\binaries\python\versions\3.13.12\python.exe`
- 如不存在则使用系统 Python

### 2. 运行 RSS 摘要脚本

执行 `scripts/linuxdo_rss_digest.py`，根据用户需求调整参数：

```bash
# 默认：处理所有源（最新+热门），最近24小时，过滤低价值分类
python scripts/linuxdo_rss_digest.py

# 只处理最新话题
python scripts/linuxdo_rss_digest.py --source latest

# 只处理热门话题
python scripts/linuxdo_rss_digest.py --source top

# 最近6小时，最多50条
python scripts/linuxdo_rss_digest.py --hours 6 --limit 50

# 只看指定分类
python scripts/linuxdo_rss_digest.py --categories 前沿快讯,开发调优

# 不过滤低价值分类
python scripts/linuxdo_rss_digest.py --no-filter
```

**源类型说明**：
- `--source latest` 或 `--source 最新话题`：只获取最新话题
- `--source top` 或 `--source 热门话题`：只获取热门话题
- `--source all`（默认）：获取所有源（最新+热门）

### 3. 输出格式要求

AI 输出必须严格按照以下格式：

```
============= 分组名称 =============
【高】标题
摘要内容（2-3句话，简洁概括核心信息）

【中】标题
摘要内容

============= 分组名称 =============
【高】标题
摘要内容
```

**重要**：
- 不要输出分类、链接、作者等额外字段
- 只输出标题和摘要
- 推荐等级用【高】/【中】/【低】标注
- 分组名称用 "=" 包裹

### 4. AI 配置

脚本支持通过环境变量配置 AI：

```bash
export AI_API_KEY=your_key
export AI_API_URL=https://your-api-endpoint/v1/chat/completions
export AI_MODEL=gpt-4o-mini  # 可选
```

如不配置，脚本只输出 JSON 而不调用 AI，此时应手动将 JSON 内容作为输入调用 AI 分析。

## 脚本参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--source SRC` | 选择 RSS 源：latest(最新话题), top(热门话题), all | all |
| `--hours N` | 抓取最近 N 小时的帖子 | 24 |
| `--no-filter` | 不过滤低价值分类 | false |
| `--categories X,Y` | 只看指定分类（逗号分隔） | 无 |
| `--limit N` | 最多处理 N 条 | 无（全部） |
| `--output-only` | 只输出 JSON，不调用 AI | false |

**源类型说明**：
- `latest` 或 `最新话题`：只获取最新话题（latest.xml）
- `top` 或 `热门话题`：只获取热门话题（top.xml）
- `all`（默认）：获取所有源（最新+热门）

## 默认过滤规则

以下分类默认被过滤（可通过 `--no-filter` 取消）：
- 搞七捻三（社区闲聊，量大低价值）
- 读书成诗（诗词创作）
- 虫洞广场（闲聊）

## 注意事项

1. RSS 源可能较大（latest.xml ~3MB/1500+ 条，top.xml ~180KB/50+ 条），脚本会自动按时间过滤
2. 如遇到 SSL 错误，脚本内置重试机制（自动忽略证书验证）
3. 输出文件保存在脚本所在目录：
   - `linuxdo_rss_filtered.json` - 过滤后的数据（包含 `source_type` 字段标识来源）
   - `linuxdo_rss_digest.md` - AI 摘要结果
4. 首次运行建议加 `--output-only` 查看数据结构，确认后再启用 AI 分析
5. 使用 `--source all`（默认）会同时获取最新话题和热门话题，数据量较大
