class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix
        rows, columns = len(matrix), len(matrix[0])
        
        res = [[0 for i in range(rows)] for i in range(columns)]

        for r in range(rows):
            for c in range(columns):
                res[c][r] = matrix[r][c]
        return res
"""
   1. create a new matrix, with row and column inverted
   2. loop through the original matrix
   3. populate the empty matrix as we loop 
    a. as we loop through row, we're populating column and vice versa

    TimeC: O(n * m)
    SpaceC: O(n * m)
"""
        