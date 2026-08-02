class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_elements = set(nums)
        return (len(nums) != len(set_elements))

"""
    bfa: check every element against all next elements
    1. for each element, loop through next elements
    2. return true if element is found again
    3. return false otherwise

    hash-map/list: check every element against hashmap of prev elements
    1. loop and check each element against list of prev elements
    2. if found, return true
    3. return false otw

    set: make a set of nums. if they are the same length, then list is distinct, else list contains duplicates
"""
         