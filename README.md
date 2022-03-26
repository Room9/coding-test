# coding-test
# 모든 풀이는 중간검증이 가능한 방식으로 진행한다. 
# 문법적으로든 연산이든 중간확인 안되는 상상풀이는 절대 금지, 잘못짚으면 돌아갈 수 없다.
# 그리드, 구현 초고난도 문제 풀기 연습필요

## 0. 알고리즘 계획(아이디어) / 시간복잡도 / 사용 할 변수명,타입 -> 코드로 구현
핵심 : 알고리즘 계획(아이디어) 떠올리는 연습 위주로
시간복잡도 : O(1) < O(logN) < O(N) < O(NlogN) < O(N^2) < O(N^3)
log의 경우 : log2를 뜻하며, 10^3 = 2^5 으로 치환가능하다

## 1. codeup-basic 100제

## 2. input / output

## 3. 그리디
현재 상황에서 가장 좋은 것만 선택하는 방법, 정당성 확보 필수
% 그리디, 완전탐색, 다이나믹 프로그래밍은 일단 가장 먼저 생각한다

## 4. 구현(완전탐색/시뮬레이션)
머릿속의 아이디어와 알고리즘을 소스코드로 바꾸는 과정
완전탐색(brute force) : 모든 경우의 수를 주저없이 계산, 탐색할 데이터가 100만개 이하이면 시도
시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행, 좌표 내 주인공의 이동
% 메모리 제약
파이썬은 직접 자료형을 지정할 필요없으며, 큰 수에 대한 연산 또한 기본으로 지원
리스트 요소 100만개 = 40mb 수준, 일반적인 문제 내 메모리 제한은 128~512mb 수준
파이썬 기준 1초에 2000만번 연산을 기준으로 삼자
% 알고리즘에서 고려해야할 것
- 시간제한 : 1초기준
- 데이터 개수
- 시간복잡도의 알고리즘 : 데이터 갯수에 따라 bigO 결정

% 완전탐색 + 순열과조합 
순열과 조합으로 모든 경우의 수를 완전탐색


## 5. BFS/DFS - 데이터 탐색 방식
자료구조 : 스택, 큐, 그래프, 트리
백트래킹 : 재귀함수, dfs 탐색 중 유망하지 않은 경로는 미리 재귀를 끝낸다
(대표문제) N-queens

[자료구조] : 데이터를 표현하고 관리하고 처리하기 위한 구조
(스택/큐) : 삽입(Push), 삭제(Pop), 오버플로, 언더플로

% 스택(Stack)
FILO 혹은 LIFO 구조
시간복잡도 O(1)
python 리스트 자료구조와 동일
삽입 - append() / 삭제 - pop()

% 큐(Queue)
FIFO 혹은 LILO 구조
시간복잡도 O(1)
python deque() 객체 사용 : 데이터 입출력 속도가 리스트 자료형에 비해 효율적
"""
from collections import deque

queue = deque()

-- queue를 리스트로 이용 시
list(queue)
"""
삽입 - append() / 삭제 - popleft()

% 재귀함수
: 자기자신을 다시 호출하는 함수
메모리의 스택공간에 동일함수가 반복호출되면서 적재되는 형태
FILO / LIFO 순서로 호출되는 함수의 결과값이 리턴된다
재귀함수는 종료조건 명시가 필수
대표예시) 팩토리얼함수 / 유클리드호재법(최대공약수)
%% 유클리드 호제법
    두 자연수 a,b(a>b)에 대해 a를 b로 나눈 나머지를 r이라고 할 때
    a와 b의 최대공약수는 b와 r의 최대공약수와 같다

% (중요) 그래프 - 2차원 배열의 탐색문제는 그래프 형태로 변경해서 고민하자!!
기본구조 : 노드(node)/정점(vertex)와 간선(edge)으로 이루어져있다.
두 노드가 간선으로 연결되어있으면 '두 노드는 인접하다'라고 표현한다.
이중 for문 이용하는 걸 늘 생각하자

그래프 표현방식 2가지 알아두기! (1)인접행렬 (2)인접리스트
(인접행렬)
2차원 배열에 각 노드의 연결 형태를 기록하는 방법
연결되어있지 않은 노드끼리는 무한(INF = int(1e9))이라고 작성한다
연결되어 있지 않은 노드끼리 형태로 표현해야해서 메모리 비효율적
특정 두 노드의 연결만 확인하는 경우 속도 우세

(인접리스트) - 가장 대중적
2차원 배열에 개별 노드에 대해 연결된 노드의 정보만 기록한다
연결된 노드에 대한 정보만 저장하기 때문에 메모리 효율적

[DFS]
https://juhee-maeng.tistory.com/25

깊이 우선 탐색, 가장 먼 곳부터 탐색한다 / 시간복잡도 O(N)
스택자료구조 + 재귀함수,반복함수 이용
    1. 탐색시작노드를 스택에 삽입하고 "방문처리" 한다
    2. 스택의 최상단노드에 (방문하지 않은 인접 노드가 있으면) 그 인접노드를 스택에 넣고 방문처리한다
    (방문하지 않은 인접노드가 없으면) 스택에서 최상단 노드를 꺼낸다
    3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다
일반적으로 인접한 노드 중에 방문하지 않은 노드가 여러 개 있으면 번호가 낮은 순서부터 처리한다.

-> 지나가는 경로를 기록하는 방식 알자
-> 백트래킹과 연관하여 생각하자

[BFS]
너비 우선 탐색, 가장 가까운 곳부터 탐색한다 / 시간복잡도 O(N)
큐자료구조, deque()를 사용한다. + 반복문 이용
    1. 탐색시작노드를 큐에 삽입하고 "방문처리" 한다
    2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다
    3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다
일반적으로 인접한 노드가 여러 개 있으면 번호가 낮은 순서부터 처리한다.

## 6. 정렬
데이터를 특정한 기준에 따라서 순서대로 나열, 이진탐색의 전처리
기본적으로 오름차순 정렬이다, 내림차순 정렬은 오름차순 정렬을 수행한 뒤 그 결과를 뒤집어 만들자
- 정렬 라이브러리(sort, sorted) 사용하는 경우
- 정렬 알고리즘의 원리를 적용하는 경우

[선택정렬]
가장 작은 데이터를 맨 앞의 데이터와 바꾸고, 그 다음 작은 데이터를 두 번째 데이터와 바꾸고...
직관적으로 이중 for문 사용하는 구조
n x (n-1) x (n-2)... x 1 => O(N^2) 시간복잡도 가진다, N 커질수록 느리다

[삽입정렬]
필요할 때만 위치를 바꾸어, 데이터가 거의 정렬되어 있을 때 매우 효과적
리스트를 하나씩 스캔해가면서 이전 요소들 사이 어느 곳에 삽입해야할지 따지며 , 필요할 때만 위치 바꾼다
O(N^2) 시간복잡도 가진다, N 커질수록 느리다

[퀵정렬] - 중요
피벗(기준, 첫번째 요소로 설정)을 설정한 다음, 왼쪽에서 큰 수를, 오른쪽에서 작은 수를 찾아 교환한다
왼쪽에서 큰 수를, 오른쪽에서 작은 수가 엇갈린 경우(= 반복문 종료 조건) 작은 데이터와 피벗을 변경한다
피벗을 기준으로 분할하여 좌 우 분할된 데이터에 대한 동일 과정 진행
재귀함수로 표현 -> 정지조건 : 퀵정렬 리스트 개수 1일 때
시간복잡도 O(NlogN) : 매우 빠르다

[계수정렬]

[python 정렬라이브러리]
sort() , sorted() 함수
병합정렬 기반으로 만듬, 최악의 경우 시간복잡도 O(NlogN) 보장

## 7. 이진정렬 : 소스코드 외우자, 노드기준 작은 게 좌측, 큰 게 우측
리스트 내에서 데이터를 빠르게 탐색하는 탐색 알고리즘
[순차탐색] - 대부분의 탐색 방식
리스트 내 데이터를 앞에서부터 순차적으로 탐색하는 기본 탐색

[이진탐색] - 이진정렬을 위한 탐색 방식
선행조건 : 리스트 내 데이터가 정렬되어있어야한다
변수 3개 이용 : 시작점 / 끝점 / 중간점 -> 중간점은 소수점 이하를 버리고 정한다 생각
탐색하려는 데이터와 중간점을 반복적으로 비교
시간복잡도 : O(logN) -> 탐색범위 1000만 단위 이상이면 이진정렬을 생각하자
구현방식 : (1) 반복문 (2) 재귀함수

% 파이썬 내 라이브러리 
bisect_left(array,x) : 정렬된 순서를 유지하면서 array에 x를 삽입할 가장 왼쪽 index를 반환
bisect_right(array,x) : 정렬된 순서를 유지하면서 array에 x를 삽입할 가장 오른쪽 index를 반환

% 트리 자료구조
용어 : 루트노드 / 말단노드 / 서브트리 / 부모노드 / 자식노드 등
그래프 자료구조의 일종으로, 계층적이고 정렬된 데이터를 다루는데 적합하다, 
큰 데이터를 처리하는 소프트웨어는 대부분 데이터를 트리 자료구조로 저장해서 이진탐색과  같은 탐색 기법을 이용한다.
DB시스템이나 파일시스템 내 데이터 관리 목적으로 사용
DB는 내부적으로 대용량 데이터 처리에 적합한 트리자료구조를 이용해 항상 데이터가 정렬되어있어, 탐색속도가 빠르다

% 이진탐색트리
트리구조 중 가장 간단한 형태
(핵심) 부모노드를 기준으로 좌측 자식노드는 항상 작고, 우측 자식노드는 항상 크다
루트노드를 기준으로 크기 비교하여 자식노드로 이동, 해당 과정을 반복해 데이터를 탐색한다
원소를 찾지 못했다면, 이진 탐색 트리에 원소가 없는 것이다.

% 이진탐색 + 파라매트릭 서치
파라매트릭 서치 : 결정 문제로 바꾸어 해결하는 기법(예,아니오)
원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제
탐색 범위를 결정 -> 중간값을 찾아 타겟값과 비교 -> 크고 작음에 따라 중간값 갱신

## 8. 다이내믹 프로그래밍(DP)

% 점화식(133p)
초기값
이전 항, 이전 항들의 현재 항에 대한 영향 확인

[탑다운]
메모제이션

[바텀업]
dp 테이블 초기화
초기값 설정
점화식 + 반복문

## 9. 최단경로
[다익스트라 최단경로 알고리즘]
(간선거리, 노드) 튜플형태로 heapq.push

% 힙구조
이진트리를 이용한 최소힙, 최대힙 구조

[플로이드 워셜 알고리즘]

## 10. 그래프 이론
(중요) 그래프는 2차원 배열에 표현한다 
(1) 경로와 방향을 고려하는 2차원인접행렬 
(2) 둘 사이의 연결여부, 연결경향을 고려하는 2차원배열 형태

[서로소 집합]
(간단한 버전)

(개선된 버전)

[크루스칼 알고리즘]
최소신장트리 / MST

[위상정렬]
DAG 증명하기(Non Cyclic)

## 11. 기타 알고리즘
[소수 여부 판결]
(최대공약수) - 유클리드호제법 / 루트값의 약수를 구하고 그 쌍을 구해서 전체 약수 구하기

[에라토스테네스의 체]
n이하에서 소수의 갯수 구하기

[투 포인터]
left와 right를 통해 원하는 값을 찾아가면서 +1,-1 씩 이동한다.
    1. 특정합을 이루는 연속하는 요소 쌍 갯수 구하기
    2. 정렬되어있는 두 리스트 합치기

[구간 합 계산]
index 별 접두사 합 prefix를 미리 계산하여 접두사 합의 차이로 구간합 구하기

[순열과 조합]

[모듈러 연산]
https://developer-mac.tistory.com/84
모듈러 합동
(a mod n +-* b mod n) mod n = (a +-* b) mod n

[링크드리스트]
https://daeun-computer-uneasy.tistory.com/20

class Node() 이용
객체명 = Node(value, next) 

## 12. SQL
[window 함수]
https://mizykk.tistory.com/121

- 집계함수 : sum / max / min / avg / count
- 순위함수 : row_number / rank / dense_rank
예시 : SELECT name, RANK() OVER (Partition by name ORDER BY salary) AS salary_rank FROM Salary WHERE salary_rank=1;
- 데이터위치바꾸기 : LAG() / LEAD()
- Ntile

[sql function 만들기]
https://wakestand.tistory.com/503

함수 정의 : create function / 인수 정의 : (인수 type) / 결과값 정의 : type
함수 로직 시작 : BEGIN / 함수 로직 끝 : END

1. RETURN(query) 방식으로 리턴하기
2. RETURN 할 변수를 decalre 하고, 
SELECT ~ INTO 변수 FROM(서브쿼리) 형식으로 변수에 쿼리결과값 넣어주고
RETURN 변수 설정

[Null 처리]
https://velog.io/@gillog/DB-MySQL-NULL-%EC%B2%98%EB%A6%ACIFNULL-CASE-COALESCE

[DATETIME, String 처리]
날짜 포맷 맞추기 : date_format(data, format)
https://lightblog.tistory.com/155
예시) date_format(DATETIME, '%Y-%m-%d')