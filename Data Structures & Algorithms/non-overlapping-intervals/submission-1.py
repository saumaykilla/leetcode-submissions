class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        output=0
        intervals= sorted(intervals,key=lambda item:[item[0]])
        cur_end = intervals[0][1]

        for i in range(1,len(intervals)):

            if intervals[i][0]>=cur_end:
                cur_end = intervals[i][1]
            else:
                output+=1
                cur_end = min(cur_end,intervals[i][1])
        
        return output

        