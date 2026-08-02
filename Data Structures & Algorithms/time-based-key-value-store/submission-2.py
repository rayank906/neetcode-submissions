class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
            1. store the key in store
            2. append [value, timestamp] pair to store

            TC: O(1)
        """
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        """
            1. l, r = 0, len(store[key]) - 1
            2. calculate mid
            3. search for value == timestamp, while l < r
            4. when l == r, return that value

            TC: O(log n)
        """
        if len(self.store[key]) == 0:
            return ""
        
        l, r = 0, len(self.store[key]) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.store[key][mid][1] < timestamp:
                l = mid + 1
            elif self.store[key][mid][1] > timestamp:
                r = mid - 1
            else:
                return self.store[key][mid][0]
        return self.store[key][r][0] if timestamp >= self.store[key][r][1] else ""

        
"""
    1. hashmap w key: key, value: [[value, timestamp]]
"""