from bankAccount import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self,customer_name, current_balance, interest_rate, account_number, routing_number):
        super().__init__(customer_name, current_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest