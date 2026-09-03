---
name: fetch-web
description: 获取网页内容并转换为 Markdown/TXT 格式。触发场景："获取内容"、"抓取文章"、"提取正文"、"转 Markdown"、"读取网页"。
dependency:
  python:
    - requests
    - beautifulsoup4
    - markdownify
---

# fetch-web

将网页 URL 转换为 Markdown 或纯文本格式，输出 JSON 结构化结果。

## How It Works

1. 接收目标 URL 和输出格式（markdown/txt/html）
2. 发起 HTTP 请求获取网页 HTML（30秒超时）
3. 使用 BeautifulSoup 移除 script/style/nav/footer/header 等非正文标签
4. 按指定格式转换内容（markdownify 转 Markdown / get_text 提取纯文本 / 原始 HTML）
5. 输出 JSON 结构化结果到 stdout，错误信息输出到 stderr

## Usage

```bash
python /mnt/skills/user/fetch-web/scripts/fetch.py <format> <url>
```

**Arguments:**

- `format` - 输出格式：`markdown`（推荐）| `txt` | `html`
- `url` - 目标网页 URL

**Examples:**

```bash
# 获取 Markdown 格式（推荐，适合文章/博客/文档）
python /mnt/skills/user/fetch-web/scripts/fetch.py markdown "https://example.com/article"

# 获取纯文本（适合摘要/关键词提取）
python /mnt/skills/user/fetch-web/scripts/fetch.py txt "https://news.example.com/story"

# 获取 HTML（调试用）
python /mnt/skills/user/fetch-web/scripts/fetch.py html "https://example.com"
```

## Output

成功时输出 JSON（stdout）：

```json
{
  "status": "success",
  "url": "https://example.com/article",
  "format": "markdown",
  "content_length": 1234,
  "content": "# Article Title\n\nArticle body text..."
}
```

失败时输出错误信息到 stderr 并以非零退出码退出：

| Exit Code | 含义 |
|-----------|------|
| 1 | 通用错误 |
| 2 | 不支持的格式 |
| 3 | 请求超时 |
| 4 | HTTP 错误（404/500等） |
| 5 | 连接失败 |
| 6 | 其他请求异常 |

## Present Results to User

1. 解析 JSON 输出中的 `content` 字段
2. 根据用户需求处理内容：摘要、翻译、分析、格式化等
3. 呈现时附上来源 URL 和内容长度信息
4. 若脚本失败，根据 exit code 给出具体建议：
   - 超时 → 建议检查网络或重试
   - HTTP 4xx → URL 可能无效
   - HTTP 5xx → 目标服务器问题，稍后重试
   - 连接失败 → 检查 URL 格式和网络

## Troubleshooting

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 请求超时 | 网络慢或页面过大 | 重试，或确认 URL 可在浏览器中打开 |
| HTTP 403 | 被反爬机制拦截 | 尝试使用 browser skill 替代 |
| 连接失败 | URL 格式错误或网络不通 | 检查 URL 是否以 http/https 开头 |
| 内容为空 | 动态渲染页面（SPA） | 使用 browser skill 替代 |
| 微信文章获取失败 | 部分文章需要登录 | 使用 browser skill 替代 |

## 适用场景

- **微信公众号文章**：大多数可直接获取，少数需登录的用 browser skill
- **静态博客/文档**：效果最佳
- **动态页面（SPA）**：不适用，请使用 browser skill
