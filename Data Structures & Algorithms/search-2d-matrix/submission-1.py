class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][len(matrix[mid]) - 1]:
                l = mid + 1
            else:
                low, high = 0, len(matrix[mid]) - 1
                while low <= high:
                    middle = (low + high) // 2
                    if target < matrix[mid][middle]:
                        high = middle - 1
                    elif target > matrix[mid][middle]:
                        low = middle + 1
                    else:
                        return True
                return False
        return False

"""
    binary search:
        1. use l, r ptr to first and last row
        2. calculate mid row, then check if target element falls between
        bounds of that row
            a. use low, high ptrs to first and last elements
            b. calculate mid
            c. check if mid == target, return true
            d. elif too small, move high to mid - 1
            e. else if too big, move low to mid + 1
            f. return False
        3. if it does, do a binary search on that row
        4. if it doesn't, if its too big, move l to mid + 1
        5. else if its too small, move r to mid - 1
        6. return False if element is never found
"""