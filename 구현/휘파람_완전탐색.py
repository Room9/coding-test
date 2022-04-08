# runtime error..하..., string 최대 20만개 조건


import sys, math


input = sys.stdin.readline

# s = {'W','H','E'}
n = input()
string =  input()

whe = list(string)
# whe = [i for i in string if i in s]

answer = 0

def find_sub_h(j):
    cnt = whe[j+1:].count('E')
    if cnt > 2:
        return math.comb(cnt,2) + math.comb(cnt,3)
    if cnt == 2 : 
        return math.comb(cnt,2)
    return 0

def find_sub_w(i):
    global answer
    hcnt = whe[i+1:].count('H')
    
    if not hcnt : return 

    for j in range(i+1,len(whe)):
        if whe[j]=='H':
            cnt = find_sub_h(j)
            if cnt == 0 : return
            answer += cnt

for i in range(len(whe)):
    if whe[i] == 'W':
        find_sub_w(i)

print(answer)