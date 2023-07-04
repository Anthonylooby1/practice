
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        self.balance - amount
        if (self.balance < 0):
            self.balance - 5
            print("insufficient funds: charging a $5 fee")
            return self
    def display_account_info(self):
        # your code here
        print(self.balance)
        return self
    def yield_interest(self):
        # your code here
        if (self.balance < 0):
            print("Not enough money")
        else: self.balance * self.int_rate
        return self


class User:
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)


    def make_deposit(self,amount):
        self.account.deposit(50)
        print(f"you made a deposit of {self.account.balance}")
        return self 
    
    def withdrawl(self,amount):
        self.account.withdraw()
        return self
    
    def display(self):
        self.account.display_account_info()
        return self


        
  

new_user = User("dan", "dan@gmail")
new_user.make_deposit(50)
