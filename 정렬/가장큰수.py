# 반례 찾기 매우 까다로운 문제
# 반례: 303, 30 일 경우
# 비교하여 정렬하는 방식 -> !비교기준 찾는 아이디어가 정확해야 함!
# 틀린 답 : 순환하여 4자리 맞춰야하는데 맨 앞자리로 비교 기준 세움

from collections import defaultdict

def sort_num(k,v):
    for i in v :
        l = len(i)
        while len(i)!=3 :
            i.append(k)
        i.append(l)
    
    v = sorted(v,key = lambda x : (x[0],x[1],x[2]),reverse=True)
    ord = [''.join(i[:i[-1]]) for i in v]
    
    return ''.join(ord)
    

def solution(numbers):
    
    dic = defaultdict(list)
    answer = ''
    
    excep = []
    
    for num in numbers :
        if num == 0 or num == 1000:
            excep.append(str(num))
            continue
        num_li = list(str(num))
        dic[num_li[0]].append(num_li)
    
    li = sorted(dic.items(),reverse = True)
    print(li)
    for k,v in li:
        ord = sort_num(k,v)
        answer += ord
        
    if excep :
        excep.sort(reverse = True)
        exc = ''.join(excep)
        answer += exc
        
    return answer

    #############3
# 모범답안
# 순환하여 4자리로 끊어서 비교해야한다.

def solution(numbers):
    answer = ''
    sum_ = 0
    tmp = []
    for number in numbers:
        c = (str(number) * 4)[:4]
        length = len(str(number))
        tmp.append((c, length))
    tmp.sort(reverse=True)
    print(tmp)
    for (c, length) in tmp:
        sum_ += int(c)
        if sum_ == 0:
            return '0'
        answer += c[:length]
    return answer