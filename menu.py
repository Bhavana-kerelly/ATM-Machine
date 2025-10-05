from functions import check_balance, deposit, withdraw, transaction_history
from accounts import accounts

# Menu List
def menu():
    while True:
        print("\n===== ATM Machine =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "4"]:
            name = input("Enter Name: ")
            pin = int(input("Enter PIN: "))

        if choice == "1":
            check_balance(accounts, name, pin)
        elif choice == "2":
            amount = float(input("Enter deposit amount: Rs"))
            deposit(accounts, name, pin, amount)
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: Rs"))
            withdraw(accounts, name, pin, amount)
        elif choice == "4":
            transaction_history(accounts, name, pin)
        elif choice == "5":
            print("Thank you..!!")
            break
        else:
            print("Invalid choice, please try again")
