from player import Player
from board import Board
import random

class Game:
    def __init__(self):
        """Initializes the players"""
        self.p1 = None
        self.p2 = None
        self.currentPlayer = None

    def setupPlayers(self):
        """Setup players with name and character."""
        name = input(f"Enter Player1's Name: ")
        symbol = random.choice(['X', 'O'])
        print(f"{name}'s symbol is: {symbol}")
        self.p1 = Player(name, symbol)

        name = input(f"Enter Player2's Name: ")
        if symbol == 'X':
            symbol = 'O'
        else:
            symbol = 'X'
        print(f"{name}'s symbol is: {symbol}")
        self.p2 = Player(name, symbol)
    
    def switchPlayer(self):
        """Switch players based on current players value."""
        if self.currentPlayer is self.p1:
            self.currentPlayer = self.p2
        else:
            self.currentPlayer = self.p1
        
    def play(self):
        """Play the game."""
        self.board = Board()
        self.setupPlayers()
        self.currentPlayer = random.choice([self.p1, self.p2])
        self.board.displayBoard()

        while True:
            #ask for valid position to move
            while True:
                position = self.currentPlayer.getMove()
                if self.board.isValidMove(position):
                    break
                else:
                    print(f"Invalid Move! Position already taken or not allowed.")
            # make a move
            self.board.move(position, self.currentPlayer.character)
            # display updated board
            self.board.displayBoard()
            # check if its a win
            if self.board.checkWin(self.currentPlayer.character):
                print(f"{self.currentPlayer.name} ({self.currentPlayer.character}) WON!")
                break
            # check if its a draw
            if self.board.isFull():
                print(f"It's a DRAW!!")
                break
            # switch players
            self.switchPlayer()


        

