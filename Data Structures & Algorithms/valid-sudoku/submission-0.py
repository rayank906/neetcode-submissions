class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {}
        colMap = {}
        x3Map = {}

        for i in board:
            for n in i:
                if n == '.':
                    continue
                elif n not in rowMap:
                    rowMap[n] = 1
                else:
                    return False
            rowMap = {}
        
        for i in range(9):
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] not in colMap:
                    colMap[board[j][i]] = 1
                else:
                    return False
            colMap = {}
        
        for square in range(9):
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in x3Map:
                        return False
                    x3Map[board[row][col]] = 1
            x3Map = {}
        return True





        
"""
    count of each digit in row, col or 3x3 <= 1
    rowMap:
        count <= 9 [loop through every list]
    colMap:
        count <= 9 [loop through every list's ith element]
    3x3Map:
        count <= 9 [loop through every 3 lists 3 times]
    
    bf check as we go:
        1. create rowMap. loop through every list in board and for every list, populate rowMap. If a value already present, return False
        2. create colMap. loop through every ith element in the list
        3. 3x3Map
            
"""        