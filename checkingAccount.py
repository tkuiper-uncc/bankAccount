from bankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, account_number=account_number, routing_number=routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, target_account):
        if amount > self.transfer_limit:
            print(f"The amount ${amount} exceeded {self.customer_name}'s transfer limit.  Max amount allowed is ${self.transfer_limit}.")
        elif amount > self.current_balance:
            print(f"Insufficient funds.  Current balance is {self.current_balance}.")
            print(f"{self.customer_name} attempted to transfer {amount} to {target_account.customer_name}.")
        else:
            self.current_balance -= amount
            target_account.current_balance += amount
            print(f"{self.customer_name} transferred ${amount} to {target_account.customer_name}.")