from savingsAccount import SavingsAccount
from checkingAccount import CheckingAccount

#create savings accounts
s1 = SavingsAccount("Damian", 2000, .03, account_number="1234", routing_number="10000001")
s2 = SavingsAccount("Tamara", 6000, .05, account_number="4321", routing_number="10000002")

#Apply interest
s1.apply_interest()
s2.apply_interest()
print("\n")
print("*** Savings Account Example 1: ***\n")

s1.print_customer_information()

print("\n")
print("*** Savings Account Example 2: ***\n")

s2.print_customer_information()

print("\n")

#Create checking accounts

c1 = CheckingAccount("Sara", 5000, account_number="3333", routing_number="10000003", transfer_limit=10000)
c2 = CheckingAccount("Anna", 4000, account_number="4444", routing_number="10000004", transfer_limit=500)

print("*** Checking Account Example 1: ***\n")

c1.print_customer_information()

print("\n")
print("*** Checking Account Example 2: ***\n")

c2.print_customer_information()

print("\n")
print("*** Transfer Scenario 1: ***\n")

#transactions
c1.transfer(800,c2)
c1.print_customer_information()
c2.print_customer_information()

print("\n")
print("*** Transfer limit exceeded example. ***\n")

c2.transfer(800,c1)
c2.print_customer_information()
c1.print_customer_information()

print("\n")
print("*** Insufficient funds example. ***\n")
c1.transfer(9000,c2)
c1.print_customer_information()
c2.print_customer_information()

print("\n")


c3 = CheckingAccount("Tessa", 2500, account_number="54321", routing_number="101010101", transfer_limit=100)
c3.print_customer_information()
c3.deposit(100)
c3.withdraw(50)

print("\n")
print("*** Insufficient funds withdrawal example. ***\n")

s4 = SavingsAccount("Samuel", 10000, interest_rate=.01, account_number="98765", routing_number="101055101")

#should trigger insufficient funds validation
s4.withdraw(10001)
s4.print_customer_information()

print("\n")
print("*** Deposit example. ***\n")

c1.deposit(100)
c1.print_customer_information()


