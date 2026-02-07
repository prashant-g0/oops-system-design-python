from bank import Bank

def admin_menu(bank, admin):
    while True:
        print("\n----Admin Panel----")
        print("1. View All Customers\n2. Create New Admins\n3. Close Customer Account\n4. Logout")

        choice = int(input("Choose an action: "))

        match choice:
            case 1:
                customers = bank.view_all_customers()
                if not customers:
                    print("No customer found.")
                else:
                    for name,balance in customers:
                        print(f"{name}: ${balance:.2f}")
                
            case 2:
                username = input("New admin username: ")
                password = input("New admin password: ")
                if bank.register_admin(username, password):
                    print("New admin created successfully.")
                else:
                    print("Username already taken.")
            
            case 3:
                username = input("Enter username to close: ")
                password = input("Enter password: ")
                success, message = bank.close_user_account(username, password)
                print(message)

            case 4:
                print("Admin logged out.")
                break

            case _:
                print("Invalid option.")



def user_menu(bank, user):
    while True:
        print("\n----User Menu----")
        print("1. View Balance\n2. Deposit\n3. Withdraw\n4. Money Transfer\n5. Logout")

        choice = int(input("Choose an action: "))

        match choice:
            case 1: 
                print(f"Balance: ${user.balance:.2f}")
            
            case 2:
                amount = float(input("Amount to deposit: "))
                if user.deposit(amount):
                    print("Deposit successful.")
                else: 
                    print("Invalid amount.")
            
            case 3:
                amount = float(input("Amount to withdraw: "))
                if user.withdraw(amount):
                    print("Withdrawal successful.")
                else: 
                    print("Invalid or insuffcient funds.")

            case 4:
                recipient_name = input("Recipient username: ")
                recipient = bank.find_user(recipient_name)
                if recipient:
                    amount = float(input("Amount to transfer: "))
                    if user.transfer(amount, recipient):
                        print("Tansfer complete.")
                    else:
                        print("Transfer failed. Check funds.")
                else: 
                    print("Recipient not found.")

            case 5:
                print("Logged out.")
                break
            
            case _:
                print("Invalid choice.")