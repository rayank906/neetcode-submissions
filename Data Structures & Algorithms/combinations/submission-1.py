class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(i, cur):
            if len(cur) == k:
                res.append(cur[:])
                return
            if i > n:
                return
            
            # Paths with i
            cur.append(i)
            helper(i + 1, cur)
            cur.pop()

            # Paths without i
            helper(i + 1, cur)
        
        helper(1, [])
        return res

"""
    1. make a global res
    2. make a helper to backtrack [i, cur]
        a. base cases
            i. if len(cur) == 2, append to copy of res and return
            ii if i > n: return
        b. append element to cur
        c. call helper with i + 1
        d. pop element from cur
        e. call helper with i + 1
    3. call helper
    4. return res

    TimeC: O(k * C(n, k))
    SpaceC: O(k)
"""
        