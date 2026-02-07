from collections import defaultdict

class Library:
    def __init__(self):
        self.admins = {"prash":"prash@1"} # username: password
        self.users = {} # username: password
        self.books = defaultdict(int) # bookname: count
        self.borrow = defaultdict(list) # bookname: username
        self.notification = defaultdict(list) # username: message
    
    def add_admin(self, username, password):
        if username not in self.admins:
            self.admins[username] = password
            return True
        
        print("Username exist!")
        return False
    
    def add_user(self, username, password):
        self.users[username] = password
    
    def add_book(self, bookname, count):
        if count >=0:
            self.books[bookname] += count
    
    def add_borrower(self, book, user):
        if self.books[book] > len(self.borrow[book]):
            self.borrow[book].append(user)
            return True
        else:
            return False
    
    def add_notification(self, username, message):
        self.notification[username].append(message)
    
    
    def check_credentials(self, username, password):
        if username in self.admins and self.admins[username] == password: 
            return "admin"
        if username in self.users and self.users[username] == password: 
            return "user"
        return None