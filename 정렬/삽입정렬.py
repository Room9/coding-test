# 삽입 정렬처럼 기준보다 이전 값들을 탐색하고, 기준을 바꿔가면서 탐색하는 문제풀이 방식 차용

def maxDifference(px):

    # 연속하는 요소끼리 비교하여 처음으로 상승하는 구간 s 확인
    s = 0

    for i in range(len(px)-1):
        if px[i] < px[i+1]:
            s = i+1
            maxd = px[i+1] - px[i]  # max difference 초기값
            minv = px[i]            # max difference를 위해 확인되어지는 min value 초기값
            break
    
    # 상승구간 없으면 return -1
    if s == 0 : return -1
    
    # 첫 상승구간s부터 요소를 탐색 
    for i in range(s,len(px)-1):
        if px[i] < px[i+1]:
            maxd = max(maxd, px[i+1]-minv)  # 이전보다 큰 값인 경우에만 maxd를 갱신할 수 있는지 확인
            continue
        minv = min(minv,px[i+1])            # 이전보다 작거나 같은 경우 minv가 갱신되는지 확인
    
    return maxd