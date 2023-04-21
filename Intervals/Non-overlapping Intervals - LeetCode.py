class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0]))
        print(intervals)
        current_interval = intervals[0]
        res = 0
        for i in range(1,len(intervals)):
            if(intervals[i][0] >= current_interval[1]):
                current_interval = intervals[i]
            else:
                if(current_interval[1] > intervals[i][1]):
                    current_interval = intervals[i]
                res += 1
        return res
