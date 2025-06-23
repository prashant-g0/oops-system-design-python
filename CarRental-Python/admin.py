from auth import Auth

class AdminInterface:
    def __init__(self, system, username):
        self.system = system
        self.username = username

    def menu(self):
        while True:
            print(f"\n--- Admin Menu ({self.username}) ---")
            print("1. Add Car")
            print("2. Remove Car")
            print("3. View Customers & Rentals")
            print("4. View Total Collected Amount")
            print("5. Create New Admin")
            print("6. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                self.add_car()
            elif choice == '2':
                self.remove_car()
            elif choice == '3':
                self.view_customers()
            elif choice == '4':
                self.view_collected()
            elif choice == '5':
                self.create_admin()
            elif choice == '6':
                break
            else:
                print("Invalid choice.")

    def add_car(self):
        name = input("Car name: ")
        if name in self.system.cars:
            print("Car already exists.")
            return
        try:
            price = float(input("Enter price: ₹"))
            self.system.cars[name] = {'price': price, 'available': True}
            print(f"{name} added successfully.")
        except:
            print("Invalid price.")

    def remove_car(self):
        print("\nAvailable Cars:")
        removable = [name for name, info in self.system.cars.items() if info['available']]
        if not removable:
            print("No removable cars.")
            return
        for i, name in enumerate(removable):
            print(f"{i + 1}. {name} - ₹{self.system.cars[name]['price']}")
        try:
            idx = int(input("Enter index to remove: ")) - 1
            car_name = removable[idx]
            del self.system.cars[car_name]
            print(f"{car_name} removed.")
        except:
            print("Invalid selection.")

    def view_customers(self):
        if not self.system.rented:
            print("No rentals currently.")
            return
        print("\n--- Customers and Their Rented Cars ---")
        for user, car in self.system.rented.items():
            print(f"{user} → {car}")

    def view_collected(self):
        print(f"\n💰 Total Collected: ₹{self.system.collected_amount}")

    def create_admin(self):
        print("\n--- Create New Admin ---")
        username = input("Admin username: ")
        if username in self.system.admins:
            print("Admin already exists.")
            return
        password = input("Password: ")
        self.system.add_admin(username, password)
        print("Admin added successfully.")
