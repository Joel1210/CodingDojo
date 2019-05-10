class User:		# here's what we have so far
    def __init__(self, name, email, amount):
        self.name = name
        self.email = email
        self.account.balance = amount
    def make_deposit(self, amount):
        self.account.balance += amount

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.balance += amount	# the specific user's account increases by the amount of the value received
        return(self)
    def withdrawal(self, amount):
        self.balance -= amount
        return(self)
    def display_account_info(self):
        print(self.balance)
        return(self.balance)
    def transfer(self, other_user, amount):
        self.balance -= amount
        other_user.make_deposit(amount)
        return(self)
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.int_rate * self.balance
        return(self)

acct1 = BankAccount(7, 1000)
acct2 = BankAccount(7, 5)

acct1.deposit(100).deposit(200).deposit(300).withdrawal(10000).yield_interest().display_account_info()
acct2.deposit(400).deposit(500).withdrawal(5).withdrawal(20).withdrawal(30).withdrawal(200).yield_interest().display_account_info()
