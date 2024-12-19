import os

class inventory():
    def __init__(self,balance = 1000):
        self.balance = balance

    def withdraw(self, amount):
        while True:  # Loop to keep asking for the withdrawal amount if it's invalid
            try:
                amount = float(input("Enter An Amount Of Money You Would Like To Withdraw: "))
                if amount <= 0:
                    print("Please Choose A Positive Number.")
                elif amount > self.balance:
                    print(f"You cannot withdraw more than your balance of {self.balance}. Please enter a valid amount.")
                else:
                    self.balance -= amount
                    print(f'{amount} has been withdrawn from your balance. New balance: {self.balance}')
                    break  # Exit the loop after a valid withdrawal
            except ValueError:
                print("Please enter a valid positive number.")
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

# Initial prompt for action (withdraw or deposit)
question = input("Would You Like To Withdraw or Deposit Money? ").lower()

# Loop to handle invalid input for withdraw/deposit
while question != 'withdraw' and question != 'deposit':
    print("Invalid input. Please type either 'withdraw' or 'deposit'.")
    question = input("Would You Like To Withdraw or Deposit Money? ").lower()

# Process the action based on the user's response
if question == 'withdraw':
    inventory_q.withdraw(1)
    inventory_q.check_balance()
elif question == 'deposit':
    inventory_q.deposit(1)
    inventory_q.check_balance()
    
      


#inventory = inventory()
#inventory.deposit(1) 
#inventory.check_balance()
#inventory.withdraw(1)