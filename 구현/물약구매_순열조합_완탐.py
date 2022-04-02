# list를 매개변수로 넣고, 지역함수에서 변동발생 시 전역변수로써 값이 바뀌어 버린다... 메모리 효율 증진 방법은..?

import sys, itertools

input = sys.stdin.readline

n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
order = [i for i in range(1,n+1)]

med = list(map(int,input().split(' ')))
med = [0]+(med)

for i in range(1,n+1):
    t = int(input())

    for _ in range(t):
        a,b = map(int,input().split(' '))
        graph[i][a] = b

npr = list(itertools.permutations(order, n))

def find_minv(medt, i):
    result = 0
    for v in i :
        result += medt[v]
        for j in range(1,len(graph[v])):
            if graph[v][j] == 0 : continue
            medt[j] = (medt[j]-graph[v][j]) if medt[j]-graph[v][j] > 1 else 1
    return result

minv = sys.maxsize

for i in npr :
    medt = med.copy()
    result = find_minv(medt, i)
    minv = min(minv, result)

print(minv)