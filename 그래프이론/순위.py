# (중요) 그래프는 2차원 배열에 표현한다 
# -> (1) 경로와 방향을 고려하는 2차원 인접행렬 (2) 둘 사이의 연결여부, 연결경향을 고려하는 2차원 배열 형태
# 여기서는 (2)를 선택한다, (승,패,알 수 없음)
# 정답 조건은 ? 2차원 배열 한 행내에 0이 하나인경우(자기자신)
# 나에게 이긴 사람은 나에게 진 사람에게 무조건 이긴다 -> 업데이트 필요

def divide(node, fight):
    win = []
    lose = []
    for i,value in enumerate(fight[node]):
        if value== -1:
            lose.append(i)
        elif value== 1:
            win.append(i)

    return [win, lose]

def solution(n, results):
    answer = n
    fight = [[0 for i in range(n)] for k in range(n)]
    cnt = dict()

    for result in results:
        winner = result[0]-1
        loser = result[1]-1
        fight[winner][loser] = 1
        fight[loser][winner] = -1

        if cnt.get(winner) == None:
            cnt[winner] = 1
        else:
            cnt[winner] +=1 
        if cnt.get(loser) == None:
            cnt[loser] = 1
        else:
            cnt[loser] +=1 
    
    #선수 별로 대결횟수 내림차순 정렬
    cnt = sorted(cnt.items(), key=lambda cnt: cnt[1], reverse=True)
    
  	
    #대결횟수가 많았던 선수 순서로 fight 2차원 리스트 데이터 갱신 
    for curNode in cnt:
        temp = divide(curNode[0],fight)
        win  = temp[0]
        lose = temp[1]
        print(win,lose)
        for i in win:
            for k in lose:
                fight[i][k] = -1
                fight[k][i] = 1
    
    for fight_row in fight:
        cnt = 0
        for item in fight_row:
            if item==0: cnt+=1
            if cnt>1: 
                answer-=1 
                break
    return answer