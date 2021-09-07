class BankAccount:
    accounts =[]
# don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        # your code here
        print("Balance: ${}".format(self.balance))
        return self
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    @classmethod
    def all_bankaccounts(cls):
        for account in cls.accounts:
            account.display_account_info()

acc1 = BankAccount(0.01, 500)
acc2 = BankAccount(0.015, 300)

acc1.deposit(20).deposit(15).deposit(40).withdraw(25).yield_interest().display_account_info()
acc2.deposit(25).deposit(20).withdraw(25).withdraw(50).withdraw(60).withdraw(80).yield_interest().display_account_info()

BankAccount.all_bankaccounts()
