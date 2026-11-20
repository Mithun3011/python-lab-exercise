
# Bank Account System

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn!")
        else:
            print("Insufficient balance!")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = Bank(name, balance)

while True:
    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        if amount > 0:
            account.deposit(amount)
        else:
            print("Enter a valid amount!")

    elif choice == "2":
        amount = float(input("Enter amount: "))
        if amount > 0:
            account.withdraw(amount)
        else:
            print("Enter a valid amount!")

    elif choice == "3":
        account.display()

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice!")
