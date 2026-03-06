class Player:
    def __init__(self, name, character):
        """Initialize the name and character of players"""
        self.name = name
        self.character = character

    def getMove(self):
        """Takes the player's move to play."""
        print(f"{self.name}'s move {(self.character)}: ")

        while True:
            try:
                move = int(input("Enter your position: "))
                if (1 <= move) and (move <= 9):
                    return move
                else:
                    print("Invalid position! Please enter in range 1-9")
            except ValueError as v:
                print("Only numbers 1-9 allowed!")
            
    
