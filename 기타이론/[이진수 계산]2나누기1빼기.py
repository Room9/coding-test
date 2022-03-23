# 이진수는 십진수로 짝수일 때 2로 나누면 한 자리씩 당겨지고, 홀수일 때 1을 빼면 첫번째 자리가 0이된다
# 효율성 점수 낮다...'011111111~~~~' 인 경우인데.. 
# 이런 경우는 1의 index를 찾으면 바로 앞의 0을 없애고 시작할 수 있다.

def solution(S):
    # write your code in Python 3.6
    
    S = list(S)
    
    #### 1부터 시작하게 아래와 같이 추가하면 효율성 증가
    t = S.index(1)
    S = S[t:]
    ####

    s = set(S)
    count = 0

    while '1' in s :
        if '0' not in s :
            count += (len(S)-1)*2+1
            break

        f_bin = S.pop()

        if f_bin == '0': count += 1    
        else : count +=1 ; S.append('0')

        s = set(S)
    
    return count