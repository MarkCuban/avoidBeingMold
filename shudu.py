from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        jie = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for row in board:
            for ch in row:
                if ch == '.':
                    hengpaijie = [x for x in jie if x not in row]
                    shupaijie = [x for x in jie if x not in [x[row.index(ch)] for x in board ]]   
                    juzhenjie = [x for x in jie if x not in [board[(board.index(row)//3)*3+i][(row.index(ch)//3)*3+j] for i in range(0, 3) for j in range(0, 3)]]
                    jies = [x for x in juzhenjie if x in hengpaijie and x in shupaijie]

                    if len(jies) > 0:
                        for j in jies:
                            tmp = []
                            for item in board:
                                tmp.append(item.copy())
                            tmp[board.index(row)][row.index(ch)] = j
                            if self.isValidSudoku(tmp) == True:
                               return True
                    return False
                else:
                    continue 
        for row in board:
            print(row)      
        return True
'''
        s = set() # columns and boxes
        row = set() # keep one row at a time 

        for i in range(0,9): # i = row

            row.clear() 
			
            for j in range(0,9): # j = column
                x = board[i][j]
                if x is not ".":                    
                    box = (i//3, j//3, x) # do the math once
                    if x in row or (j, x) in s or box in s:
                        return False

                    row.add(x)
                    s.add((j, x)) # j is the column number. We can see if x is 
                    s.add(box) 

        return True      
'''

                   



sol = Solution()

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
'''
board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board = [
    [".","8","7","6","5","4","3","2","1"],
    ["2",".",".",".",".",".",".",".","."],
    ["3",".",".",".",".",".",".",".","."],
    ["4",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".",".","."],
    ["6",".",".",".",".",".",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    ["8",".",".",".",".",".",".",".","."],
    ["9",".",".",".",".",".",".",".","."]
    ]
'''    
print(sol.isValidSudoku(board))