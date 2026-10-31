accounts = {}

def create_account():
    name = input("Enter account holder name: ")

    if name in accounts:
        print("An account already exists with this name.")
        return

    while True:
        try:
            initial_deposit = float(input("Enter initial deposit amount: "))
            if initial_deposit >= 0:
                break
            print("Initial deposit cannot be negative.")
        except ValueError:
            print("Please enter a valid amount.")

    accounts[name] = {
        "balance": initial_deposit,
        "transactions": [f"Account created with Rs. {initial_deposit:.2f}"]
    }

    print(f"\nAccount created successfully for {name}.\n")


def deposit_money():
    name = input("Enter account holder name: ")

    if name not in accounts:
        print("Account not found.")
        return

    while True:
        try:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                break
            print("Deposit amount must be greater than zero.")
        except ValueError:
            print("Please enter a valid amount.")

    accounts[name]["balance"] += amount
    accounts[name]["transactions"].append(f"Deposited Rs. {amount:.2f}")

    print(f"\nRs. {amount:.2f} deposited successfully.")
    print(f"New balance: Rs. {accounts[name]['balance']:.2f}\n")


def withdraw_money():
    name = input("Enter account holder name: ")

    if name not in accounts:
        print("Account not found.")
        return

    while True:
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif amount > accounts[name]["balance"]:
                print("Insufficient balance.")
            else:
                break
        except ValueError:
            print("Please enter a valid amount.")

    accounts[name]["balance"] -= amount
    accounts[name]["transactions"].append(f"Withdrew Rs. {amount:.2f}")

    print(f"\nRs. {amount:.2f} withdrawn successfully.")
    print(f"Remaining balance: Rs. {accounts[name]['balance']:.2f}\n")


def check_balance():
    name = input("Enter account holder name: ")

    if name not in accounts:
        print("Account not found.")
        return

    print(f"\nAccount holder: {name}")
    print(f"Current balance: Rs. {accounts[name]['balance']:.2f}\n")


def show_transactions():
    name = input("Enter account holder name: ")

    if name not in accounts:
        print("Account not found.")
        return

    print(f"\nTransaction history for {name}:")
    for transaction in accounts[name]["transactions"]:
        print("-", transaction)
    print()


while True:
    print("\n===== BANK ACCOUNT MANAGEMENT SYSTEM =====")
    print("1. Create account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. Show transaction history")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        show_transactions()
    elif choice == "6":
        print("Thank you for using the Bank Account Management System!")
        break
    else:
        print("Invalid choice. Please try again.")