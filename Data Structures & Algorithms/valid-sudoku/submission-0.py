class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(x,y,val):
            #check the row
            for i in range(0,9):
                if i==x:
                    continue
                else:
                    if board[i][y]==val:
                        return False
            #check the column
            for j in range(0,9):
                if j==y:
                    continue
                else:
                    if board[x][j]==val:
                        return False
            a=x//3 *3
            b=y//3 *3
            for i in range(a,a+3):
                for j in range(b,b+3):
                    if i==x and j==y:
                        continue
                    else:
                        if board[i][j]==val:
                            return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if check(i,j,board[i][j])==False:
                        return False
        return True
