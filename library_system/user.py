class UserFunctions:
    def __init__(self, system):
        self.system = system
    
    def all_books(self):
        if not self.system.books: 
            print("No available books")
            return 
        
        print("---All books---")
        for book, count in self.system.books.items():
            print(f"{book} : {count}")
        return
    
    def borrow_book(self, user):
        book = input("Enter book name: ")
        if book not in self.system.books or self.system.books[book] == 0: 
            print(f"{book} is not available!")
            return False
        
        self.system.add_borrower(book, user)
        self.system.books[book] -= 1
        print(f"{book} borrowed successfully!")
        return True
    
    def return_book(self, user, book):
        if user in self.system.borrow[book]:
            self.system.borrow[book].remove(user)
            self.system.books[book] += 1
            print(f"{book} returned successfully!")
            return True
        else: 
            print("You didn't borrow this book!")
            return False
    
    def view_notifications(self, user):
        if user not in self.system.notification: 
            print("No notifications for you!")
            return
        
        msgs = self.system.notification[user]
        print("0: last notification;\n1: all notifications;\nq: exit")
        while True:
            choice = input("Enter choice: ").lower()

            if choice == "q": return 

            elif choice == "0" and msgs:
                print(f"Last: {msgs[-1]}")

            elif choice == "1":
                print("\nAll notifications: ")
                for i, msg in enumerate(msgs, 1):
                    print(f"{i}. {msg}")
            else: 
                print("Invalid choice!")

class UserInterface:
    def __init__(self, system, username):
        self.system = system
        self.username = username
        self.functions = UserFunctions(system)
    
    def menu(self):
        print(f"Welcome {self.username}!")
        while True:
            print("1. See all Books\n2. Borrow a Book\n3. Return a book\n4. Notifications\n5. Logout")
            try:
                choice = int(input("Enter choice number: "))
                if choice == 1:
                    self.functions.all_books()
                elif choice == 2:
                    self.functions.borrow_book(self.username)
                elif choice == 3:
                    book = input("Enter book name: ")
                    self.functions.return_book(self.username, book) 
                elif choice == 4:
                    self.functions.view_notifications(self.username)
                elif choice == 5: 
                    print("Logged out.")
                    break
                else: 
                    print("Invalid choice! Try again.")
            except ValueError:
                print("Enter a number!")
            
        