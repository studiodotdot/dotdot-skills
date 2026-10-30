#!/usr/bin/env python3
"""PDF 페이지 수 세기 — `python3 pdf_pages.py 덱.pdf`

`/Type /Page` 글자를 세면 틀린다. Chrome PDF는 페이지 객체를 압축 스트림 안에 넣고,
슬라이드 본문 텍스트에 같은 글자가 있으면 그것까지 세어 버린다.
대신 페이지 트리의 뿌리(`/Type /Pages`이면서 `/Parent`가 없는 사전)를 찾아
그 `/Count` 값을 읽는다. 압축 스트림(객체 스트림)도 풀어서 찾는다.
"""
import re
import sys
import zlib

PAGES_DICT = re.compile(rb'<<(?:[^<>]|<<[^<>]*>>)*?/Type\s*/Pages\b(?:[^<>]|<<[^<>]*>>)*?>>', re.S)
COUNT = re.compile(rb'/Count\s+(\d+)')


def count_pages(path):
    data = open(path, 'rb').read()
    chunks = [re.sub(rb'stream\r?\n.*?endstream', b'', data, flags=re.S)]
    for m in re.finditer(rb'stream\r?\n(.*?)endstream', data, re.S):
        try:
            chunks.append(zlib.decompress(m.group(1)))
        except zlib.error:
            pass
    roots = []
    for chunk in chunks:
        for d in PAGES_DICT.finditer(chunk):
            body = d.group(0)
            c = COUNT.search(body)
            if c and b'/Kids' in body and b'/Parent' not in body:
                roots.append(int(c.group(1)))
    if not roots:
        raise SystemExit('페이지 트리를 찾지 못했다 — 손상됐거나 지원하지 않는 PDF')
    return roots[-1]   # 증분 저장된 PDF는 옛 뿌리가 앞에 남을 수 있어 마지막 것을 쓴다


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    print(count_pages(sys.argv[1]))
