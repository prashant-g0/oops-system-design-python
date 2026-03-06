from game import Game

def app():
    """Runs the game and gives the choice the continues or stop."""
    while True:
        choice = input("Start a new game? (Y/N): ").strip()
        if choice in ['Y', 'y']:
            print("Let's see who's the real XO master!")
            game = Game()
            game.play()
        elif choice in ['N', 'n']:
            print("We had a great play! See you soon.")
            break
        else:
            print("Invalid choice! Try again")

if __name__ == "__main__":
    app()