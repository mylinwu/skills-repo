#!/usr/bin/env python
"""
网页内容获取工具 - 支持 Markdown/TXT/HTML 格式输出，JSON 结构化结果
用法: python fetch.py <markdown|txt|html> <url>
"""
import json
import sys

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

TIMEOUT = 30


def fetch_url(url, format_type='markdown'):
    """获取 URL 内容并转换为指定格式，返回 JSON 结果"""
    try:
        response = requests.get(url, headers=DEFAULT_HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        # 移除脚本和样式
        for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
            tag.decompose()

        # 微信公众号：提取正文区域
        is_wechat = 'mp.weixin.qq.com' in url
        if is_wechat and soup.find(id='js_content'):
            # 微信文章正文在 #js_content 内
            content_node = soup.find(id='js_content')
            # 移除底部工具栏、二维码等噪音
            for sel_id in ['js_pc_qr_code', 'js_share_source', 'js_tags', 'js_old_review']:
                el = content_node.find(id=sel_id)
                if el:
                    el.decompose()
            for cls in ['rich_media_tool', 'profile_container', 'rich_media_tool_area']:
                for el in content_node.find_all(class_=cls):
                    el.decompose()
            # 移除底部推荐文章链接
            for el in content_node.find_all(id='js_tags'):
                el.decompose()
        else:
            content_node = soup.body or soup

        if format_type == 'html':
            content = str(content_node)
        elif format_type == 'txt':
            text = content_node.get_text(separator=' ', strip=True)
            content = ' '.join(text.split())
        elif format_type == 'markdown':
            content = md(str(content_node), heading_style='ATX', strip=['img'])
        else:
            print(f"Error: 不支持的格式 '{format_type}'，请使用 markdown/txt/html", file=sys.stderr)
            sys.exit(2)

        result = {
            'status': 'success',
            'url': url,
            'format': format_type,
            'content_length': len(content),
            'content': content
        }
        print(json.dumps(result, ensure_ascii=False))

    except requests.exceptions.Timeout:
        print(f"Error: 请求超时（{TIMEOUT}秒），URL: {url}", file=sys.stderr)
        sys.exit(3)
    except requests.exceptions.HTTPError as e:
        code = e.response.status_code if e.response is not None else 'unknown'
        print(f"Error: HTTP {code} - {url}", file=sys.stderr)
        sys.exit(4)
    except requests.exceptions.ConnectionError:
        print(f"Error: 无法连接到 {url}，请检查 URL 或网络", file=sys.stderr)
        sys.exit(5)
    except requests.exceptions.RequestException as e:
        print(f"Error: 请求失败 - {e}", file=sys.stderr)
        sys.exit(6)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python fetch.py <markdown|txt|html> <url>", file=sys.stderr)
        sys.exit(1)

    fmt = sys.argv[1].lower()
    url = sys.argv[2]
    fetch_url(url, fmt)
