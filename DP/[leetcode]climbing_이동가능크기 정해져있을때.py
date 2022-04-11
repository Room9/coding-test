# 이동 가능크기가 1,2로 정해져 있을 때
# d(n) = d(n-k) + k에서 n으로 이동하는 경우 -> 를 고려하여 접근하는 가장 흔하고 좋은 문제
# 1,2칸만 움직일 수 있을 때 점화식 + 초기값

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 : return 1
        if n == 2 : return 2
        d = [0] * 46
        d[1], d[2] = 1, 2
        
        if n > 2 : 
            i = 2
            while i != n :
                i += 1
                d[i] = d[i-1]+d[i-2]
        return d[i]