# 최단경로갯수 = 우상향으로 갈때만 고려하여 하나씩 더해가면서 갯수 구하자

# DP + bfs 사용

# 인접리스트 아닌 2차원 배열 인접행렬의 bfs인 경우
# -> 재귀보다 이중 for문을 쓰며 스캔하는게 더 빠르고 직관적이다.

# (중요)모듈러연산(mod연산)의 경우 모듈러 합동을 이용해 값마다 계산해주는 것이 속도향상에 좋다.

#1 시간초과 발생 : 재귀사용 + dp memozation 미사용, 
# (1,1)부터 (m,n)까지 계산하는데 (1,1) 이후 부분이 지속 재계산 됨

def dfs(route, x, y,m,n):
    
    if x == n and y == m:
        return 1
    if x > n or y > m:
        return 0
    if route[x][y] == -1 :
        return 0
    
    return dfs(route, x+1, y,m,n)%1000000007 + dfs(route, x, y+1,m,n)%1000000007
    
def solution(m, n, puddles):
    answer = 0
    route = [[0]*(m+1) for i in range(n+1)]
    
    for p in puddles :
        route[p[1]][p[0]] = -1
    
    answer = dfs(route,1,1,m,n)
    
    return answer%1000000007


# 2 재귀사용하면서 (x,y)를 key로 이용한 memozation 실행
def solution(m, n, puddles):
    answer = 0
    #  a.한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 dict 초기화
    #  b.메모 초기값 설정
    info = dict([((2, 1), 1), ((1, 2), 1)])
    for puddle in puddles:
        info[tuple(puddle)] = 0

    def func(m, n):
        print(info)
       
        if m < 1 or n < 1:
            return 0
        # c. (중요)이미 계산한 적 있는 문제라면 그대로 반환
        if (m, n) in info:
            return info[(m, n)]
        # 메모된게 아니라면 점화식으로 계산
        return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))
    return  func(m, n) % 1000000007

# 3. 2차원 인접행렬에 대한 bfs를 이중 for문으로 스캔하면서 진행
# 하나씩 구해서 더하가면서 최단거리 도출 방식

def solution(m, n, puddles):
    graph = [[0] * (m+1) for _ in range(n+1)]  
    graph[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 초기값이나 장애물에 해당하는 좌표면 continue
            if [i,j] in puddles or [i, j] == [1, 1]:
                continue
            else:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]
    return (graph[-1][-1] % 1000000007)