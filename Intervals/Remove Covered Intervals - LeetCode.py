class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        current_interval = intervals[0]
        res = 0
        for i in range(1,len(intervals)):
            if(intervals[i][0] >= current_interval[1]):
                current_interval = intervals[i]
            else:
                if(current_interval[1] >= intervals[i][1]):
                    print(current_interval,intervals[i])
                    res+=1
                else:
                    current_interval = intervals[i]
        return len(intervals)-res
