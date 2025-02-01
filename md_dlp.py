# 源代码 (md_dlp.py):
#!/usr/bin/env python3

import argparse
import requests
import re
import os

def extract_content(raw_content):
    """提取标题和内容"""
    # 提取标题
    title_match = re.search(r'Title: (.*?)$', raw_content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else 'Untitled'

    # 提取源 URL
    url_match = re.search(r'URL Source: (.*?)$', raw_content, re.MULTILINE)
    source = url_match.group(1).strip() if url_match else ''

    # 提取正文内容
    content_match = re.search(r'Markdown Content:\n(.*)', raw_content, re.DOTALL)
    content = content_match.group(1).strip() if content_match else raw_content

    return title, source, content

def format_markdown(title, source, content):
    """格式化为标准 markdown"""
    return f"""---
title: {title}
source: {source}
---

{content}
"""

def fetch_and_save(url):
    """
    从给定URL获取内容并保存为标准格式的markdown文件
    """
    # 添加基础URL前缀
    base_url = "https://r.jina.ai/"
    full_url = base_url + url

    try:
        # 获取内容
        response = requests.get(full_url)
        response.raise_for_status()
        raw_content = response.text

        # 解析内容
        title, source, content = extract_content(raw_content)

        # 格式化为标准 markdown
        md_content = format_markdown(title, source, content)

        # 生成安全的文件名
        safe_title = re.sub(r'[/\\:*?"<>|]', '_', title)
        filename = f"{safe_title}.md"

        # 保存文件
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"Content saved to: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content: {e}")
        exit(1)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Download content and save as standard markdown file'
    )
    parser.add_argument('url',
                       help='URL to fetch (will be prefixed with https://r.jina.ai/)')

    args = parser.parse_args()
    fetch_and_save(args.url)

if __name__ == "__main__":
    main()
