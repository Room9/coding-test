# 이진트리 기반의 최소힙 라이브러리
# 모든 부모 노드는 그의 자식 노드보다 값이 작거나 큰 이진트리(binary tree) 구조인데, 
# 내부적으로는 인덱스 0에서 시작해 k번째 원소가 항상 자식 원소들(2k+1, 2k+2) 보다 작거나 같은 최소 힙의 형태로 정렬된다.   
import heapq 

list = [4,2,7,9,1]
heap = heapq.heapify(list)

heapq.heappush(heap,'추가원소')
heapq.heappop(heap)

# 최대힙 구현 : - 이용

import heapq 

list = [4,2,7,9,1]
list = list(map(lambda x : x*-1,list))
heapq.heapify(list)

while heap:
    heapq.heappop(heap)*-1

# k번째 최대값 or 최소값
import heapq

def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3)) 

# 4 return됨