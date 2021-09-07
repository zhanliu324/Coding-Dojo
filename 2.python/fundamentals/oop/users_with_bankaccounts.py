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

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            'acc1': BankAccount(int_rate=0.02, balance=0),
            'acc2': BankAccount(int_rate=0.05, balance=200)
            }

    def make_deposit(self, amount, acc):
        self.account[acc].deposit(amount)
        return self

    def make_withdrawal(self, amount, acc):
        self.account[acc].withdraw(amount)
        return self
    
    def display_user_balance(self):
        for acc in self.account.keys():
            print(f"User: {self.name}, Account: {acc}, Balance: ${self.account[acc].balance}")
        return self

    def transfer_money(self, other_user, amount, acc):
        self.account[acc].withdraw(amount)
        other_user.account[acc].deposit(amount)
        return self

tom = User("Tom")

tom.make_deposit(100,'acc2')
tom.display_user_balance()