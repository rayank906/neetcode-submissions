class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        curSum = 0
        res = 0

        prefix[0] += 1

        for i in range(len(nums)):
            curSum += nums[i]
            if (curSum - k) in prefix:
                res += prefix[(curSum - k)]
            prefix[curSum] += 1
        return res
        

"""
    1. go through all possible first element subarrays
    2. make a hashmap for prefix sums and count of prefix sums
    3. whenever we encounter a subarray sum, subtract from k and check
    if that result exists in hashmap.
    4. if it does, add its count to res
    5. repeat for all subarrays of the first element

    Edge case:
        sum 0 should be initialized to 1 because the empty subarray is a
        valid subtraction. (Happens when subarray sum is == k)

    TimeC: O(n)
    SpaceC: O(n)
"""
        