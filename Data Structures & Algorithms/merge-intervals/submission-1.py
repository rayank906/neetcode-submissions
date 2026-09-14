class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            - sort the intervals
            - loop with prev interval

            - prev before curr
                interval end <= curr start
                - add prev to res
                - update prev to curr
            - prev interval merges with curr
                - update prev with min(starts), max(ends)
            - append prev to res
        """
        intervals.sort()
        prev = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if prev[1] < start:
                res.append(prev)
                prev = [start, end]
            else:
                prev = [min(prev[0], start), max(prev[1], end)]
        res.append(prev)
        return res