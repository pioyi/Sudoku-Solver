class Sudoku():
    def __init__(self,Board):
        self.Board = Board

    def is_valid(self,n,pos):
        # Checking the row
        for i in range(len(self.Board[pos[0]])):
            if self.Board[pos[0]][i] == n and pos[1] != i:
                return False

        # Checking the column
        for i in range(len(self.Board)):
            if self.Board[i] != pos[0] and self.Board[i][pos[1]] == n:
                return False

        # Cheking the number's block
        row,col = [i//3*3 for i in pos]
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if self.Board[i][j] == n and (i,j) != pos:
                    return False  

        return True
        
    def print_board(self):
        for i in range(len(self.Board)):
            if i % 3 == 0 and i != 0:
                print("------|-------|------")
            print(' | '.join(' '.join(str(b).replace("0"," ") for b in self.Board[i][a*3:a*3+3]) for a in range(3)))

    def search_empty(self):
        for row in range(9):
            for col in range(9):
                if not self.Board[row][col]:
                    return (row, col)
        return None

    def solve(self):
        if (w:= self.search_empty()):
            row,col = w
            for i in range(1,10):
                if self.is_valid(i,(row,col)):
                    self.Board[row][col] = i

                    if self.solve():
                        return True

                    self.Board[row][col] = 0
            return False
        return True

Sudoku1 = Sudoku([
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
])

print("\n")
Sudoku1.print_board()
print("\nRunning...\n")
Sudoku1.solve()
Sudoku1.print_board()