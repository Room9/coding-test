# 집합(set)
a = {}
b= {}

a.add(b) : a u b
a.intersect(b) : a n b


# deque
from collections import deque

d =deque(list)
d.popleft()
d.pop()
d.appendleft()
d.append

# 반복문 종료조건을 무엇으로 설정할지가 매우 중요하다
while (종료조건) :


################

#해쉬형태 문제풀이

# list 내 요소를 key / 요소들의 갯수를 value로 가지는 dict 생성
import collections
collections.Counter(list)

# dict에서 특정 key 제거 시
dict.pop('key')

# dict에 없는 key가 들어오면 default로 key 생성하겠다
defaultdict(list)

# get함수는 선언된 dict에서 출력하고자 하는 key가 있으면, 그에 해당하는 value를 출력해줍니다.
# 또한, 출력하고자 하는 key가 없으면, 오류가 아닌 None을 출력합니다.
value = dict.get(key)


################

import math

#올림
math.ceil()

#나누기 몫
a//b

## a>0,b>0 일 때
-(a//b) = -(a//b+1)

# 나누기 나머지
a%b

################


# min, max

min(a,b)
max(a,b)
max(list)