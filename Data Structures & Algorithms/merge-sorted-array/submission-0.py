class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m > n:
            for i in range(len(nums2)):
                nums1[m + i] = nums2[i]
        else:
            for j in range(len(nums2)):
                nums1[m + j] = nums2[j]
        return nums1.sort()
        
        
"""

"""
        