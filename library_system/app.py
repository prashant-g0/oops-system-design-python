from system import Library
from auth import Authentication
from user import UserInterface
from admin import AdminInterface

class App:
    def run(self):
        lib = Library()
        auth = Authentication(lib)

        while True:
            print("---Library Management System---")
            print("1. Login\n2. Register as User\n3. Exit")
            try:
                ch = int(input("Enter your choice number: "))
            except ValueError:
                print("Invalid Input! Try again.")
                continue

            if ch == 1:
                role, user = auth.login()
                if role == "user":
                    UserInterface(lib, user).menu()
                elif role == "admin":
                    AdminInterface(lib, user).menu()
            elif ch == 2:
                user, password = auth.register()
                lib.add_user(user, password)
            elif ch == 3:
                print("Thanks! Goodbye.")
                break
            else:
                print("Invalid choice! Try again.")

if __name__ == "__main__":
    App().run()