class CarRentalSystem:
    def __init__(self):
        self.admins = {'admin': 'admin123'}
        self.users = {}  # username: password
        self.cars = {}  # car_name: {'price': float, 'available': bool}
        self.rented = {}  # username: car_name
        self.collected_amount = 0.0  # total money collected from all rentals

    def add_admin(self, username, password):
        self.admins[username] = password

    def add_user(self, username, password):
        self.users[username] = password

    def check_credentials(self, username, password):
        if username in self.admins and self.admins[username] == password:
            return 'admin'
        elif username in self.users and self.users[username] == password:
            return 'user'
        return None
