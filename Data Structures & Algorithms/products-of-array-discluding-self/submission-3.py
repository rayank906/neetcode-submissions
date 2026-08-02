class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            1. calculate prefix product and put in prefix array
                a. keep track of product, init to 1
                b. for num in nums
                c. prefix.append(product)
                d. product *= num
            2. calculate suffix product and put in suffix array
                a. keep track of product, init to 1
                b. for num in nums, loop in reverse
                c. suffix[i] = product
                d. product *= num
            3. for num in nums
            4. add prefix[i] + suffix[i]
        """
        prefix = [0 for i in range(len(nums))]
        suffix = [0 for i in range(len(nums))]
        
        # calc prefix
        prod = 1
        for i in range(len(nums)):
            prefix[i] = prod
            prod *= nums[i]
        # calc suffix
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = prod
            prod *= nums[i]
        print(prefix, suffix)

        # calc result
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res
        