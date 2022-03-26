# DFS 함수 정의, STACK과 재귀 사용
def dfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

# 인접리스트 - 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

#혹은
graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }


# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)


###########################################

# DFS, 반복문 사용
def stack_dfs(start_vertex):
	visited = []
	stack = [start_vertex]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
				visited.append(vertex)
				for item in graph[vertex]:
					stack.append(item)
	return visited

##################
  # DFS, 개별 경로 확인

https://juhee-maeng.tistory.com/25 확인

paths = []

def dfs_paths(graph, start, end, visited=[]):
    # 그 전에 방문했던 노드들을 기록하고
    # 이번 차례 방문하는 노드를 새로 추가한다.
    # (중요) 1. append와 +[]의 차이는? 2. visited = dfs()과 그냥 dfs()의 차이는?
    # +[]는 visited가 재귀를 거치면서 개별 주소를 참조하여 따로 list 취급됨
    # .append는 visited가 재귀를 거치면서 동일 주소 참조하여 동일 list에 쌓임, 기억하며 쌓인다
    visited = visited + [start] 
    
    #도착할 경우, paths에 경로를 기록한다.
    if start == end:
        paths.append(visited)
    
    #현재 노드의 자손 노드들 중, 방문하지 않은 노드들에 대해 재귀 호출
    for node in graph[start]:
        if node not in visited:
            dfs_paths(graph, node, end, visited)

graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# return 예시 형식
[['A', 'B', 'E', 'H'], ['A', 'C', 'F', 'H']]


#############

# 백트래킹 : 더 이상 갈 수 있는 길이 없을 때 빠르게 포기 
# + 진행 경로까지 확인

def solution(tickets):
    # tickets을 dict형태 graph로 변환
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)

    # stack 초기값 설정
    # 진행 path 초기값 설정
    stack = ["ICN"]
    path = []

    while len(stack) > 0:
        # stack에서 last out하고
        top = stack[-1]

        # 더 이상 갈 경로가 없는 조건일 때 stack에서 pop하여 path로 넣음
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        # 더 깊이 탐색할 곳 확인하여 stack에 쌓으면서, dict의 밸류값에서 빼주면서 visit처리 대체
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]


