from main import *
from bank import Bank

def app():
    bank = Bank()
    while True:
        print("\n===Welcome to SimpleBank===")
        print("\n1. Register User\n2. Login as User\n3. Login as Admin\n4. Exit")

        choice = int(input("\nSelect an option: "))

        match choice:
            case 1:
                username = input("Choose username: ")
                password = input("Choose password: ")
                if bank.register_user(username, password):
                    print("User registered successfully.")
                else:
                    print("Username already exists.")

            case 2:
                username = input("Username: ")
                password = input("Password: ")
                user = bank.login_user(username, password)
                if user:
                    print(f"Welcome, {username}!")
                    user_menu(bank, user)
                else:
                    print("Login failed.")

            case 3:
                username = input("Admin username: ")
                password = input("Admin password: ")
                admin = bank.login_admin(username, password)
                if admin:
                    print(f"Welcome Admin: {username}")
                    admin_menu(bank, admin)
                else:
                    print("Admin login failed.")

            case 4:
                print("Thank you for banking with us!")
                break

            case _:
                print("Invalid option.")

if __name__ == "__main__":
    app()
            