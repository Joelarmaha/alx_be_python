class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited: ${amount}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount < self.account_balance and amount is not None:
            self.account_balance -= amount
            return f"Withdrew:${amount}"
        else:
            print("Insufficient funds.")

    def display_balance(self):
        return f"Current Balance:${self.account_balance}"
