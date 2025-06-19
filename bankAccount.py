class BankAccount:
    bank_title = "Wellsfargo"

    def __init__(self, customer_name, current_balance, minimum_balance=0, account_number=None, routing_number=None):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  #protected
        self.__routing_number = routing_number  #private

    def deposit(self, amount):
        self.current_balance += amount
        print(f"Deposited ${amount} to Customer: {self.customer_name}.")
        print(f"{self.customer_name}'s current balance is {self.current_balance}.")

    def withdraw(self, amount):
        if amount <= self.current_balance:
            self.current_balance -= amount
            print(f"Withdrawn {amount} to {self._account_number}.")
            print(f"Current balance is {self.current_balance}.")
        else:
            print(f"Withdrawal of ${amount} failed. \nInsufficient funds.")
            print(f"Current account balance is {self.current_balance}.")
            print()

    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: ${self.current_balance}")
        print(f"Account #: {self._account_number}")




