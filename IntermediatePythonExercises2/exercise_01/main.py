from BankAccount import BankAccount

account = BankAccount("My Account", 1000)

account.deposit(500)
account.withdraw(200)
print(account.get_balance())
