class BankAccount:
    def __init__(self, account_balance, withdraw, deposit, current_balance):
        self.display_balance = None
        self.account_balance = account_balance
        self.deposit = deposit
        self.withdraw = withdraw
        self.current_balance = current_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance = self.account_balance + amount
            return f' Deposited: {amount}'
        else:
            return "not valid"

    def withdraw(self, amount):
        if amount != 0:
            self.account_balance = self.account_balance - amount
            print(f' Deposited: {amount}')
        else:
            return "not valid"

    def display_balance(self, current_balance):
        self.display_balance = current_balance
        return f' Current Balance: {self.display_balance()}'


import sys
from bank_account import BankAccount


def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
