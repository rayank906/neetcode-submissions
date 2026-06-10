class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
            1. for every num
            2. init list of perms
            3. for every perm
                4. for every number, insert at each idx of len(perms) + 1
                5. save the perm to a temp of perms
            6. save temp to perms
            7. return the perms
        """
        perms = [[]]
        for n in nums:
            temp = []
            for p in perms:
                for j in range(len(p) + 1):
                    p.insert(j, n)
                    temp.append(p.copy())
                    p.pop(j)
            perms = temp
        return perms
        