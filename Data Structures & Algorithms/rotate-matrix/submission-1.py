class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        top, bottom = l, r

        while l < r:
            for i in range(r - l):
                temp = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = temp
            l += 1
            r -= 1
            top, bottom = l, r

"""
    1. using two ptrs l, r
    2. while l < r,
    3. loop r - 1 times
        a. using top and bottom and bottom for the columns:
        b. store the top left element
        c. take the 4th element and place it in the first position
        d. take the third element and place it in the 4th position
        e. take the 2nd element and place it in the 3rd position
        f. take the temp and place it in the second
    4. shift r and l inwards, moving top and bottom inwards to access
    the inner matrix
    5. when r and l cross positions, there is no valid matrix left to explore

    TimeC: O(n^2) where n is the number of rows/cols
    SpaceC: O(1)
"""
        