class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        
        def sort(n, intervals):
            intervals.sort()
        sort(n, intervals)
        arr = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in intervals:
            if i[0]<=end:
                end=max(end, i[1])
            else:
                arr.append([start, end])
                start = i[0]
                end = i[1]

        arr.append([start, end])
        return arr
                