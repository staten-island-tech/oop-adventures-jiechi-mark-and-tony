import os

class inventory():
    def __init__(self,balance = 1000):
        self.balance = balance

    def withdraw(self, amount):
        try:
            amount = float(input("Enter An Amount Of Money You Would Like To Withdraw"))
            if amount <=0:
                print("Please Choose A Positive Number")
            elif self.balance < amount:
                print("You're not that rich, buddy! Insufficient funds.")
            else:
                self.balance -= amount
                print(f'{amount} has been withdrawn from your balance. New balance: {self.balance}')
            
        except ValueError:
            print("Please Choose A Positive Number")
    def check_balance(self):
       print(f'Your current balance is: {self.balance}')



        
    

    def deposit(self, amount):
       while True:
        try:#Chat Gpt suggested to handle an error using try and except
         amount =  float(input("Choose An Amount You Would Like To Deposit:"))
         if amount > 0:

            self.balance += amount
            
            
            print(f'{amount} has been added to your balance. New balance: {self.balance}')
            break
         else:
            print("Choose a valid amount 🐊")
        except ValueError:
           print("Please enter a valid positive number.")


inventory_q = inventory()
question = input("Would You Like To Withdraw or Deposit Money? ")   
if question == 'withdraw':
    inventory_q.withdraw(1)
    inventory_q.check_balance
elif question == 'deposit':
    inventory_q.deposit(1)
    inventory_q.check_balance
else:#should probably use a while loop instead if wrong and break somewhere
    input("Hey Thats Not A Valid Answer Try Again:")
    
      


#inventory = inventory()
#inventory.deposit(1) 
#inventory.check_balance()
#inventory.withdraw(1)