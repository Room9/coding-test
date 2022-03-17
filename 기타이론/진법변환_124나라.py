# 10진법을 n진법로 변경할 때는, n으로 나눠가면서 나머지: 1~(n-1)와 몫을 사용하자, divmod 사용
# 2진법 전환 생각해서 먼저 연산한게 뒷부분에 붙도록 정렬한다 
# 10진수 a와 n진법이 주어질 때
def from_base10(a,n):
    digits = []

    while a>0:
        a , m = divmod(a,n)
        digits.insert(0,str(m))
    
    return digits

# 124나라는 3진법으로 변경한다.
# 3진법으로 변환하는 코드 짜기

# (1)
# 사용 가능한 숫자(정석풀이에서 나머지)가 1, 2, 4여서 0이 없으므로 0, 1, 2가 1, 2, 4로 하나씩 밀림
# 3으로 나눈 나머지를 1,2,3이라고 생각전환해서
# 0으로 나누어 떨어질 때 3으로 바꾸고 몫에서 1 빼기(올림이 하나 밀리니 앞 자리수도 하나 적어짐)
# 리스트 전체 3을 4로 바꾸기

def solution(n):
    result = []
    while n:
        t = n % 3
        if not t:
            t = 3
            n -= 1
        result.append(str(t))
        n //= 3

    for i in range(len(result)):
        if result[i] == '3':
            result[i] = '4'
    return ''.join(result[::-1])


# (2) 3진법 mod 나머지인 0,1,2를 인덱스로하여 1,2,4와 매핑되어있음 
# 3진법 mod 몫으로 다음 연산 반복 -> 2진법 전환 생각해서 먼저 연산한게 뒷부분에 붙도록 정렬한다 
def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]

#############################

def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer