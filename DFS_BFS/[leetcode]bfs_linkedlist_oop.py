
# (중요) Node라는 class를 정의했으므로, Node type의 객체를 이용한다는 것을 알 수 있다.
# Node객체.val / Node객체.neighbors
# linkedlist 형태로 Node객체(현재값, 연결되는값)로 만들라고 주어짐.
class Node {
    public int val;
    public List<Node> neighbors;
}

# Node 객체 생성 
<__main__.Node object at 0x7f22e47baf50>])

# bfs 사용 / input : Node type / output : Node type
# (중요) 최종적으로 clone이 가지려는 형태 : {1: Node(1,[2,4]), 2: Node(2,[1,3]), 3:Node(3.[2,4]), 4:Node(4,[1,3])}
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        # copy해서 2차원 리스트(dict 형태)만들 clones 생성(key = node의 값, value = Node객체(node의 값, 연결된 node 값 있는 리스트))
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]  # pop 한 node 객체의 neighbor 값(초기값은 [])을 설정          
            
            for ngbr in cur.neighbors:
                if ngbr.val not in clones: # clones에 시작 index(key)없으면 방문 안 한 것이므로
                    clones[ngbr.val] = Node(ngbr.val, []) # 방문처리하고, node 객체의 neighbor 초기값 [] 설정
                    q.append(ngbr) # q에 다음 Node 객체 넣는다
                
                # 현재 node의 value인 Node객체의 neighbor(리스트)에 연결된 Node객체의 value를 넣는다
                cur_clone.neighbors.append(clones[ngbr.val]) 

        return clones[node.val]