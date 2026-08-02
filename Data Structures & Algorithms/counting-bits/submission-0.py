class Solution:
    def countBits(self, n: int) -> List[int]:
        """
            Counting bits for every num from 0 to n
            1. loop through 0 to n
            2. for every n,
                a. while n > 0:
                    count += 1 if n & 1 == 1
                    bit shift to right
                b. append count to ans
            3. return ans

            TC: O(n * m) where m is avg num of operations to count bits on a val
            SC: O(n) for res, O(1) without
        """

        ans = []
        for i in range(0, n + 1):
            count = 0
            while i > 0:
                if i & 1 == 1:
                    count += 1
                i = i >> 1
            ans.append(count)
        
        return ans
        