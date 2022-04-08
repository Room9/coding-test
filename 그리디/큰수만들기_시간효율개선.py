
# 부분함수를 잘라가면서 max 값을 가져와야했다.
# 시간효율부분에서 에러가 났다.

# (1) for 반복문 의심
# 1 -> 2 로 for list 구문 대신 deque 이용한 while q 를 이용했으나 시간개선 효과 없음
# 1,000,000개 수준 반복문이라 for 구문 문제는 아님

# (2) max 값 찾는 부분 의심
# max(list) 부분이 가장 의심됨, 999,999인 경우 한 번 반복 시 O(nlogn)이어도 백만수준 연산... 
# 2 -> 3으로 9이면 더 이상 최대값 찾지 않도록 변경

#1
def solution(number, k):
    n = len(number)
    
    answer = ''
    
    t = list(number[:k])
    
    for i in number[k:]:
        t.append(i)
        mx = max(t)
        idx = t.index(mx)
        answer += mx
        t = t[idx+1:]        
        
    return answer

##################
#2

from collections import deque

def solution(number, k):
    n = len(number)
    
    answer = ''
    
    t = list(number[:k])
    q = deque(number[k:])
    while q:
        i = q.popleft()
        t.append(i)
        mx = max(t)
        idx = t.index(mx)
        answer += mx
        t = t[idx+1:]        
        
    return answer

##################
#3

def solution(number, k):
    n = len(number)
    
    answer = ''
    
    t = list(number[:k])
    q = deque(number[k:])
    while q:
        mx = '0'
        idx = 0
        i = q.popleft()
        t.append(i)
        
        for j, m in enumerate(t):
            if int(m) == 9 :
                mx = m
                idx = j
                break
            if int(m) > int(mx) :
                mx = m
                idx = j
        
        answer += mx
        t = t[idx+1:]        
        
    return answer