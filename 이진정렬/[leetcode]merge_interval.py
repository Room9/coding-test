# 최대 갯수 100000까지 list를 만들고, interval 시작점에 2가 들어가도록 설정, 다시 interval로 변환
# 문제점 : 다시 interval로 변환시키는 과정에서 경우의 수를 따지기 매우 복잡했다
# 큰 list 를 만들고 시작함으로써 속도와 메모리 효율 매우 낮아짐

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        d = [0]*100001
     
        result = []
        
        for interval in intervals :
            if interval[1]-interval[0] == 0 :
                d[interval[0]] = 2
                continue
            d[interval[0]] = 2
            d[interval[0]+1:interval[1]+1] = [1]*(interval[1]-interval[0])
        
        if d[newInterval[0]] == 2:
            pass
        if d[newInterval[0]] == 0:
            d[newInterval[0]] = 2
        if newInterval[1]-newInterval[0] != 0:
            d[newInterval[0]+1:newInterval[1]+1] = [1]*(newInterval[1]-newInterval[0])
            

        r = []
        for i in range(len(d)):
            
            if len(r)==0 and d[i]==2:
                r.append(i)
                continue
            if len(r)==1 :
                if d[i]==0 :
                    r.append(i-1)
                    result.append(r)
                    r=[]
                    continue
                if d[i]==2:
                    r.append(i-1)
                    result.append(r)
                    r=[]
                    r.append(i)
                    continue
                if i == len(d)-1 :
                    r.append(i)
                    result.append(r)
                    r=[]
                    continue

        return result

# 탐색수가 많아 메모리와 속도 효율 감소 시 -> 이진트리 혹은 메모제이션을 생각하자!
# 이진정렬 이용 + len(intervals)==0 은 초반에 미리 처리해주자

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
		# Time complexity would be improved to O(logN) if we use binary search for finding index
        # start = 시작점 중 new[0]와 크거나 같은 첫 번째 index
        start = 0
        while start < len(intervals) and intervals[start][1] < newInterval[0]:
            start += 1
        
        # end = 끝점 중 new[1]와 작거나 같은 첫 번째 index
        end = len(intervals) - 1
        while start <= end and newInterval[1] < intervals[end][0]:
            end -= 1
        
        # min/max를 이용한 비교 -> 양 끝점 예외상황 확인필요
        newInterval = [ \
            min(intervals[start][0], newInterval[0]) if start < len(intervals) else newInterval[0], \
            max(intervals[end][1], newInterval[1]) if -1 < end else newInterval[1] \
        ]
        return intervals[:start] + [newInterval] + intervals[end+1:]
        