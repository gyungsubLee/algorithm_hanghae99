# 참조)https://growingarchive.tistory.com/157

# 변수로 지칭하고 실행 시 '()' 붙여라.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = {}

for _ in range(n):
    site, pw = input().split()
    data[site] = pw

for _ in range(m):
    input_site = input().rstrip()
    print(data[input_site])