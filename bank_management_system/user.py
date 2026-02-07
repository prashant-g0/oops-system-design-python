class User:
    def __init__(self, username, password):
        self.user = username
        self._password = password
        self.balance = 0.0

    def check_password(self, password):
        return self._password == password
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def transfer(self, amount, recipient):
        if self.withdraw(amount):
            recipient.deposit(amount)
            return True
        return False
    
    