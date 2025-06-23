class Auth:
    def __init__(self, system):
        self.system = system

    def login(self):
        print("\n--- Login ---")
        username = input("Username: ")
        password = input("Password: ")
        role = self.system.check_credentials(username, password)
        if role:
            print(f"Welcome, {username} ({role})!")
            return role, username
        else:
            print("Invalid credentials.")
            return None, None

    def register_user(self):
        print("\n--- Register User ---")
        username = input("Username: ")
        if username in self.system.users:
            print("Username already exists.")
            return
        password = input("Password: ")
        self.system.add_user(username, password)
        print("User registered successfully.")
