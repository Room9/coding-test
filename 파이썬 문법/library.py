# heap
# heap은 최소값이나 최대값만을 찾기위한 자료구조 : 부모 자식노드의 관계를 정립해 만듬
# 이진정렬트리는 좌노드는 작고 우노드는 크도록 정렬 : 좌우노드의 관계를 정립해 만듬


# 비트연산자
https://codetorial.net/python/operators/bitwise_operator.html

# i와 j는 십진수, 비트연산자는 십진수끼리 비트처럼 계산해서 십진수를 리턴하는 것

i << 1 , i >> 1 : 2진수로 생각할 때, 2배 혹은 1/2배
i^j : XOR # (서로 다를 때만 참)
i&j : AND
i|j : OR

# 집합(set)
a = {}
b= {}

a.add(b) : a u b
a.intersect(b) : a n b

sett = {a,b}


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

dic = {key:value}

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


###########
list

# python 에서 일정구간 array 값을 한번에 바꾸고싶을 때 다음과 같은 방식으로 진행

a = [0, 0, 0, 0, 0, 0, 0]

b = [1, 2, 3]

# a라는 array에서 0번째에서 2번째까지 b의 array 값으로 바꾸고싶을땐

a[0:2] = b
print(a)
# a = [1, 2, 3, 0, 0, 0, 0]

# 연속된 수를 담는 list 만들고 싶을 때
list(range(1, 11))

