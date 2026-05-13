from Account import Account

class Savings_Account(Account):
    def __init__(self,owner,balance=0):
        super().__init__(owner,balance)
        self.interest_rate = 9.8

        #withdraw limit attribute
        self.withdraw_limit = 100

    def apply_interest(self):
        interest = self.get_balance()*self.interest_rate
        self.deposit(interest)
        print(f"interest of {interest} applied. new balance {self.get_balance()}")

        #overridden withdraw method with improved error messages
    def withdraw(self,amount):
        if amount > self.withdraw_limit():
         print(f"withdrawal exceeds limit of {self.withdraw_limit}")
        elif amount > self.get_balance():
         print(f"withdrawal exceeds balance of {self.get_balance()}")
        else:
         super().withdraw(amount)




