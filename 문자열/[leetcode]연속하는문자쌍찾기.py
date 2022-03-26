
# 연속하는 중복되지 않는 가장 긴 문자열 길이
# 각 요소부터 시작해서 가장 긴 길이를 구하면 시간복잡도 상승
# seen = []을 따로 정의해서 중복되는 문자열까지만 삭제해주는 방식 사용 -> del seen[0:idx+1]
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = []
        longest = 0
        for letter in s:
            if letter in seen:
                idx = seen.index(letter)
                del seen[0:idx+1]
            seen.append(letter)
            longest = max(longest,len(seen))
        return(longest)


############
# left / right 투포인트 이용해 r - l 의 값을 리턴
#1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = dict()
        max_len = 0
        l = 0
        r = 0
        while l < len(s) and r < len(s):
            if s[r] not in dic:
                dic[s[r]] = True
                r += 1
                max_len = max(max_len, r - l)
            else:
                dic.pop(s[l])
                l += 1
        return max_len

#2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0 ; j=1 ; ans=0
        while j<=len(s):
            if len(set(s[i:j]))!=len(s[i:j]): ans=max(ans,j-i-1) ; i+=1 ; j=i+1
            else: j+=1
        return max(ans,j-i-1)





