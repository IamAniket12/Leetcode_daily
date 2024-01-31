class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       dr = defaultdict(list)
       dc = defaultdict(list)
       drc = defaultdict(list)
       for r in range(len(board)):
           for c in range(len(board[0])):
                if board[r][c] in dr[r] or board[r][c] in dc[c] or board[r][c] in drc[(r//3,c//3)]:
                   return False
                elif board[r][c]==".":
                    continue   
                else:
                    dr[r].append(board[r][c])
                    dc[c].append(board[r][c])
                    drc[(r//3,c//3)].append(board[r][c])
       return True                

       
        