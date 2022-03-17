# testdome 샘플문제
# 이진트리의 루트노드가 주어지고 하부 트리 내 value가 있는가?
# namedtuple 로 node 주어짐
# bfs로 탐색 -> 정확도 맞았으나 시간효율 틀림
# 시간효율줄이기 방식
# -> 이진트리 특성임을 이용해, 노드의 value가 주어진 value와 비교해 큰 지 작은지에 따라 나머지 절반만 마져 bfs탐색한다

import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    q = collections.deque([root])
    
    while q:
        r = q.popleft()
        if r.value == value:
            return True
        if r.value > value:
            if r.left:
                q.append(r.left)
            continue
            
        if r.value < value :
            if r.right:
                q.append(r.right)
            continue

    return False

        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))