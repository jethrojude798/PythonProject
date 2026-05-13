class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


        def deposit(self,amount):
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount} ")
            else:
                print("invalid deposit amount")

        def withdraw(self, amount):
             if 0 < amount <= self.balance:
                        self.balance -= amount
                        print(f"Withdrawal of ${amount} successful. New balance is ${self.balance} ")
             else:
                 print("invalid withdrawal amount")

        def get_balance(self):
            return self.balance


