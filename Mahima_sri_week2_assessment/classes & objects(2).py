class BankAccount:
    def __init__(self, balance=0):
        self.balance= balance
        
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"The amount deposited is:{self.balance}")
        else:
            print(f"The amount you entered is invalid ")
            
    def withdraw(self,amount):
        if amount>0 :
            if self.balance>=amount:
                self.balance-=amount
                print(f"The amount withdrawn is:{self.balance}")
            else:
                print("insufficent fund in the account")
        else:     
            print(f"The amount you entered is invalid")
        
a=BankAccount()
a.deposite(1000)
a.withdraw(500)
