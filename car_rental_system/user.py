class UserInterface:
    def __init__(self, system, username):
        self.system = system
        self.username = username

    def menu(self):
        while True:
            print(f"\n--- User Menu ({self.username}) ---")
            print("1. View Available Cars")
            print("2. Rent a Car")
            print("3. Return Car")
            print("4. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                self.view_cars()
            elif choice == '2':
                self.rent_car()
            elif choice == '3':
                self.return_car()
            elif choice == '4':
                break
            else:
                print("Invalid choice.")

    def view_cars(self):
        available = [(car, info) for car, info in self.system.cars.items() if info['available']]
        if not available:
            print("No cars available.")
            return
        print(f"\nAvailable Cars ({len(available)} total):")
        for i, (car, info) in enumerate(available, 1):
            print(f"{i}. {car} - ₹{info['price']}")

    def rent_car(self):
        if self.username in self.system.rented:
            print("You already have a car rented. Return it first.")
            return

        available = [(car, info) for car, info in self.system.cars.items() if info['available']]
        if not available:
            print("No cars available.")
            return

        print("\nAvailable Cars:")
        for i, (car, info) in enumerate(available, 1):
            print(f"{i}. {car} - ₹{info['price']}")
        try:
            idx = int(input("Select car index: ")) - 1
            car_name, car_info = available[idx]
            car_info['available'] = False
            self.system.rented[self.username] = car_name
            self.system.collected_amount += car_info['price']
            print(f"Successfully rented {car_name} for ₹{car_info['price']}. (No refunds)")
        except:
            print("Invalid input.")

    def return_car(self):
        if self.username not in self.system.rented:
            print("You have no car to return.")
            return
        car_name = self.system.rented[self.username]
        self.system.cars[car_name]['available'] = True
        del self.system.rented[self.username]
        print(f"You returned {car_name}. No refund will be issued.")
