class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0


    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)    

user1 = User("Joe", "Joe.Biden@outlook.com")
user2 = User("James", "James.Henley@outlook.com")
user3 = User("Jane", "Jane.Smith@outlook.com")

user1.make_deposit(21)
user1.make_deposit(76)
user1.make_deposit(6000)
user1.display_user_balance()

user2.make_deposit(86)
user2.make_deposit(2084)
user2.make_withdrawal(73)
user2.make_withdrawal(88)
user2.display_user_balance()

user3.make_deposit(408)
user3.make_withdrawal(488)
user3.make_withdrawal(274)
user3.display_user_balance()

user1.transfer_money(user3, 200)
user1.display_user_balance()
user3.display_user_balance()
