---
name: lenny-newsletter-analyzer
description: 分析 Lenny's Newsletter 文章内容，生成综合报告并提炼核心思想。触发场景：用户要求分析 Lenny's Newsletter 文章、生成报告、总结思想、了解产品经理或 AI 相关趋势。输入为 https://www.lennysnewsletter.com/archive?sort=new 任意 URL 或首页，按流程抓取内容后输出结构化分析报告。
---

抓取并分析 Lenny's Newsletter 文章，生成结构化综合报告，提炼核心思想与趋势洞察。

## Workflow

1. 使用 `WebFetch` 抓取目标 URL（支持首页或任意文章页）
2. 解析页面内容，获取前10条文章数据，提取：标题、作者、日期、点赞数、文章正文
3. 逐个分析每篇文章
4. 输出综合分析报告

## Report Structure

综合报告包含以下模块：

### 1. 高热度文章分析表

| 文章标题 | 作者 | 日期 | 👍 |

### 2. 核心思想提炼（每篇 200-500 字）

- 简述背景与作者
- 提炼核心洞察（2-3 条）
- 引用关键原文（用 > 引用块）
- 附实操要点或行动建议

### 3. 趋势综合判断（Top 3）

| 趋势 | 重要性 | 原因 |

## Output Format

使用中文输出。报告使用 Markdown 格式，关键引文用 `>` 引用块，表格用 Markdown table。

## Notes

- 如果遇到登录问题请停止流程并通知用户
- 多数文章为付费内容（Substack 订阅），抓取到的可能为摘要或开头段落
- 可用 `agent-browser` 技能打开浏览器访问完整付费内容（如浏览器可用）
- 首页按最新排序参数：`?sort=new`
- 首页按热度排序参数：`?sort=new`
