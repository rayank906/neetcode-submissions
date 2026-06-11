class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
            0. init subsets, curr
            1. sort nums
            2. recursive helper [i, curr]
                3. if i >= len(nums):
                    4. append curr to subsets
                    5. return
                6. append num to curr
                7. recurse with curr
                8. pop num from curr
                9. loop until next number
                10. recurse without curr
        """
        subsets, curr = [], []
        nums.sort()

        def recurse(i, curr):
            if i >= len(nums):
                subsets.append(curr.copy())
                return
            
            # choose element
            curr.append(nums[i])
            recurse(i + 1, curr)

            # not choose element / skip duplicates
            curr.pop()
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            recurse(i + 1, curr)
        
        recurse(0, curr)
        return subsets