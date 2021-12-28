#bank account challange



class Account():

    def __init__(self, owner="John Doe", balance=0):
        self.owner = owner
        self.balance = balance
        # print("Account owner: ", owner, "\nAccount balance: ", balance)
    
    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: PLN {self.balance}"

    def deposit(self, dep_amount):
        self.balance += dep_amount
        print("Added {} to the balance".format(dep_amount))

    def withdrawal(self, wit_amount):
        if wit_amount <= self.balance:
            self.balance -= wit_amount
            print("Withdrawal accepted!")
        else:
            print("Not enough on your balance, Dear Sir, to withdraw PLN {}.".format(wit_amount))

print(Account)
print(Account())
acct1 = Account("Rob", 1990)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(2001)
print(acct1)
acct1.withdrawal(1000)
print(acct1)
