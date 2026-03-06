class Board:
    def __init__(self):
        """Initializes the board with positions 1-9"""
        self.grid = [['1', '2', '3'],
                ['4', '5', '6'],
                ['7', '8', '9']]
        
    def displayBoard(self):
        """Display the board position"""
        for row in self.grid:
            for cell in row:
                print(f"| {cell}", end=" ")
            print("|\n-----------\n")

    def move(self, position, character):
        """Takes board position and makes with player's symbol"""
        row = (position-1)//3
        col = (position-1)%3

        self.grid[row][col] = character  
    
    def isValidMove(self, position):
        """Checks if the given position is correct to play a move or not."""
        row = (position-1)//3
        col = (position-1)%3

        if self.grid[row][col].isdigit():
            return True

        return False

    def isFull(self):
        """Check if the board is full and out of moves."""
        for row in self.grid:
            for cell in row:
                if cell.isdigit():
                    return False
        return True
    
    def checkWin(self, character):
        """Checks if the current character wins for the current board."""
        winning_lines = [
            # Rows
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            # Columns
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            # Diagonals
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)]
        ]
        
        return any(all(self.grid[r][c] == character for r, c in line) for line in winning_lines)

            