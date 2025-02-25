class Client:
    def __init__(self,name,acc_balance):
        self.name=name
        self.acc_balance=acc_balance
        
    def deposit(self,amount):
        if amount>0:
            self.acc_balance +=amount
            print(f"{amount}successfully deposited,current amount={self.acc_balance}")
        else:
            print(f"amount must be greater than zero")
            
    def withdraw(self,amount):
        if amount>0 and amount<=self.acc_balance:
            self.acc_balance-=amount 
            print(f"The withdrawel amount is {amount},current balance={self.acc_balance}")
        else:
            print(f"Written amount is insufficient")
            
    def left_amount(self):
        print(f"Your remaining credits={self.acc_balance}")
        
        
client=Client("Abdullah",2300)
client.deposit(500)
client.withdraw(700)
client.left_amount()
client.withdraw(100)
    
            
