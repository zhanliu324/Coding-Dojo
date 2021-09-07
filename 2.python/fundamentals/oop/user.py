class User:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

tom = User('Tom', 100)
jerry = User('Jerry', 200)
katy = User('Katy', 20)

tom.make_deposit(20)
tom.make_deposit(10)
tom.make_deposit(50)
tom.make_withdrawal(25)
tom.display_user_balance()

jerry.make_deposit(100)
jerry.make_deposit(20)
jerry.make_withdrawal(15)
jerry.make_withdrawal(55)
jerry.display_user_balance()

katy.make_deposit(500)
katy.make_withdrawal(25)
katy.make_withdrawal(45)
katy.make_withdrawal(120)
katy.display_user_balance()

tom.transfer_money(katy, 55)
tom.display_user_balance()
katy.display_user_balance()