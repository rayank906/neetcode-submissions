class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
            - interval before curr
                end of new < start of curr
                - add interval to res
                - add curr to res
            - interval after curr
                end of curr < start of interval
                - add curr to res
            - overlap with curr
                - interval = min(starts) and max(ends)
        """
        res = []
        iStart, iEnd = newInterval[0], newInterval[1]

        for i in range(len(intervals)):
            start, end = intervals[i]
            if iEnd < start:
                res.append([iStart, iEnd])
                return res + intervals[i:]
            elif end < iStart:
                res.append([start, end])
            else:
                iStart, iEnd = min(iStart, start), max(iEnd, end)
                
        res.append([iStart, iEnd])
        return res
        