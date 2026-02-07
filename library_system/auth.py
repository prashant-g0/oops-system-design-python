class Authentication:
    def __init__(self, system):
        self.system = system

    def login(self):
        print("---Login---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        role = self.system.check_credentials(username, password)

        if role: 
            print(f"Welcome {username}! ({role})")
            return role, username
        else:
            print("Invalid credentials!!!")
            return None, None
        
    def register(self):
        print("---Register---")
        while True:
            username = input("Enter username: ")
            if username not in self.system.users:
                break
            print("Username already exists! Try different.")

        password = input("Enter password: ")
        return username, password
