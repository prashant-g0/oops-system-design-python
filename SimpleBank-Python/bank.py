from user import User
from admin import Admin

class Bank:
    def __init__(self):
        self.users = {}
        self.admins = {}

        self.admins['admin'] = Admin('admin', 'admin123')

    def register_user(self, username, password):
        if username in self.users or username in self.admins:
            return False
        self.users[username] = User(username, password)
        return True
    
    def register_admin(self, username, password):
        if username in self.users or username in self.admins:
            return False
        self.admins[username] = Admin(username, password)
        return True
    
    def login_user(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            return user
        return None
    
    def login_admin(self, username, password):
        admin = self.admins.get(username)
        if admin and admin.check_password(password):
            return admin
        return None
    
    def find_user(self, username):
        return self.users.get(username)
    
    def view_all_customers(self):
        return [(username, user.balance) for username, user in self.users.items()]
    
    def close_user_account(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            if user.balance == 0:
                del self.users[username]
                return True, "Account closed successfully."
            else:
                return False, "Balance must be zero to close the account."
        return False, "Invalid credentials or user not found."
    