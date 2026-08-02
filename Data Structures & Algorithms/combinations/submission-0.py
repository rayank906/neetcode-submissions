class Solution:
    def helper(self, i, curSet, combs, n, k):
        if len(curSet) == k:
            combs.append(curSet[:])
            return
        if i > n:
            return
        
        for j in range(i, n + 1):
            curSet.append(j)
            self.helper(j + 1, curSet, combs, n, k)
            curSet.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        curSet, combs = [], []
        self.helper(1, curSet, combs, n, k)
        return combs

"""
    1. create res array
    2. call helper
        a. if len(curSet) == K, append a copy and return
        b. if i > n, return
        c. for i in range(i, n + 1):
            curSet.append(i)
            helper(i + 1)
            curSet.pop()
    3. return res array

    TimeC: O(k * C(n, k))
    SpaceC: O(k * C(n, k)), O(k) for recursive call stack
"""
        