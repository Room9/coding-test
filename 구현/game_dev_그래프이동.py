import sys

input = sys.stdin.readline

# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 서 : 3, 남 : 2, 동 : 1, 북 : 0 문제에서 정의됨
# 북, 동, 남, 서 방향 정의 : index -1로 가면 왼쪽으로 가도록 정렬
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 : 반시계 방향으로 direction(dx,dy의 인덱스) 이동
# 위에서 정의한 direction을 전역변수 global로 받겠다
def turn_left():
    global direction
    direction -= 1 
    if direction == -1:
        direction = 3 #0에서 왼쪽 -1 가면 3이 되도록

count = 1
turn_time = 0 # 네방향 모두 못가는지 확인하기 위한 기준변수
while True:
    # 1. 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 2. 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 3. 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        # 뒤로간다 = 현재 방향으로 앞으로 가는 것을 뺀다!
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)