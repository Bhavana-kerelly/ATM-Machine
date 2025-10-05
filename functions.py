# Balance Checking
def check_balance(accounts, name, pin):
    for acc in accounts:
        if acc["name"] == name and acc["pin"] == pin:
            print(f"Balance for {name}: Rs{acc['balance']}")
            return
    print("Invalid name or PIN")

# Money Deposit
def deposit(accounts, name, pin, amount):
    for acc in accounts:
        if acc["name"]== name and acc["pin"]== pin:
           acc["balance"] += amount
           acc["trasactions"].append(f"Deposited Rs{amount}")
           print(f" Deposited Rs {amount}. New balance: Rs{acc['balance']}")
           return 
    print("Invalid name or PIN")

# Money Withdraw using name, pin
def withdraw(accounts, name, pin, amount):
    for acc in accounts:
        if acc["name"] == name and acc["pin"] == pin:
            if acc["balance"] >= amount:
                acc["balance"] -= amount
                acc["transactions"].append(f"Withdrew ₹{amount}")
                print(f"Withdrew Rs{amount}. New balance: Rs{acc['balance']}")
            else:
                print("Insufficient balance")
            return
    print("Invalid name or PIN")

# Displaying Transaction History of particular user
def transaction_history(accounts, name, pin):
    for acc in accounts:
        if acc["name"] == name and acc["pin"] == pin:
            print(f"Transaction History for {name}:")
            if not acc["transactions"]:
                print("No transactions yet.")
            else:
                for t in acc["transactions"]:
                    print("-", t)
            return
    print("Invalid name or PIN")
