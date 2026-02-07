class AdminFunctions:
    def __init__(self, system):
        self.system = system
    
    def create_admin(self, username, password):
        if self.system.add_admin(username, password):
            print(f"{username} added successfully!")
        return
    
    def view_admin(self):
        print("All admins: ")
        for user in self.system.admins.keys():
            print(f"{user}")
            return
    
    def view_user(self):
        print("All users: ")
        for user in self.system.users:
            print(f"{user}")
        return

    def add_book(self):
        book = input("Enter book name: ")
        try:
            count = int(input("Enter count of book: "))
            self.system.add_book(book, count)
            print(f"{book} added successfully!")
        except ValueError:
            print("Invalid count!")
        return
    
    def remove_book(self):
        book = input("Enter book name: ")
        if book in self.system.books:
            del self.system.books[book]
            print(f"{book} removed successfully!")
            return True
        print(f"{book} not found!")
        return False
    
    def all_book(self):
        if not self.system.books: 
            print("No available books")
            return 
        
        print("---All books---")
        for book, count in self.system.books.items():
            print(f"{book} : {count}")
        return
    
    def all_borrow(self):
        if not self.system.borrow:
            print("No borrows currently!")
            return
        
        print("Borrows: ")
        for book, user in self.system.borrow.items():
            print(f"{book} : {','.join(user)}")
    
    def notify(self): 
        user = input("Enter username: ")
        if user not in self.system.users: 
            print("User not found!!")
            return

        msg = input("Enter message: ")
        self.system.add_notification(user, msg)
        print(f"{user} notified successfully!")
        return True
    
class AdminInterface:
    def __init__(self, system, username):
        self.system = system
        self.username = username
        self.functions = AdminFunctions(system)
    
    def menu(self):
        
        while True:
            print("1. Add books\n2. Remove books\n3. See all books\n4. See all borrowers\n5. Send notifications\n6. Create new admins")
            print("7. View all users\n8. View all admins\n9. Logout")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.functions.add_book()
                elif choice == 2:
                    self.functions.remove_book()
                elif choice == 3:
                    self.functions.all_book()
                elif choice == 4:
                    self.functions.all_borrow()
                elif choice == 5:
                    self.functions.notify()
                elif choice == 6:
                    user = input("Enter username: ")
                    password = input("Enter password: ")
                    self.functions.create_admin(user, password)
                elif choice == 7:
                    self.functions.view_user()
                elif choice == 8:
                    self.functions.view_admin()
                elif choice == 9: 
                    print("Goodbye!")
                    break
                else: print("Invalid choice! Try again.")
            except ValueError: print("Enter number!")
