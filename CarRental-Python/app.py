from system import CarRentalSystem
from auth import Auth
from admin import AdminInterface
from user import UserInterface

def app():
    system = CarRentalSystem()
    auth = Auth(system)

    while True:
        print("\n=== Car Rental System ===")
        print("1. Login")
        print("2. Register (User)")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            role, username = auth.login()
            if role == "admin":
                AdminInterface(system, username).menu()
            elif role == "user":
                UserInterface(system, username).menu()
        elif choice == '2':
            auth.register_user()
        elif choice == '3':
            print("Thank You for using Car Rentals-- Aapke sapno ki udaan!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    app()