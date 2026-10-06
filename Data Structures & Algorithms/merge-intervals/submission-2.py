class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda item: [item[0]])

        cur_start = sorted_intervals[0][0]
        cur_end = sorted_intervals[0][1]
        res = []
        print(sorted_intervals)
        for i in range(1,len(sorted_intervals)):
            if sorted_intervals[i][0] <=cur_end:
                cur_end = max(cur_end , sorted_intervals[i][1])
            else:
                res.append([cur_start,cur_end])
                cur_start = sorted_intervals[i][0]
                cur_end = sorted_intervals[i][1]
        
        res.append([cur_start,cur_end])


        return res


        