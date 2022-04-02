# return 값을 1000000007로 나눠라 = 연산 내에서 나누면서 진행해라, mod 규칙 이용
# 런타임에러 발생...

import sys
from collections import defaultdict

input = sys.stdin.readline

graph = defaultdict(list)

n,m = map(int, input().split(' '))

num = [0] + list(map(int,input().split(' ')))

for _ in range(n-1):
    a,b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

total = []

def dfs(visit, i, j):
    visit = visit + [i]

    if i == j : total.append(visit) ; return

    for node in graph[i]:
        if node not in visit:
            dfs(visit, node, j)

for _ in range(m):
    i,j = map(int, input().split(' '))

    visit = []

    dfs(visit,i,j)

for path in total:
    result = ''
    for p in path:
        result += str(num[p])
    print(int(result)%1000000007)