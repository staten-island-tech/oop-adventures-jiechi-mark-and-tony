import random
numbers = list(range(1,71)) 
class ticket():
    def __init__(self):
        self.guess = []
        self.random_number = []
    def lotto(self):
        self.guess = [input("Choose a number from 1-70: ") for _ in range(5)] #Chatgpt made it loop 5 times instead of 5 lines of the same code
        return self.guess
    def rlotto(self):
        self.random_number = [random.choice(numbers) for _ in range(5)]
        print(self.random_number)
        return self.random_number
    def reveal(self):
        if self.guess == self.random_number:
            print("win")
        elif self.guess != self.random_number:
            print("lose")
tickets = ticket()
tickets.rlotto()
tickets.lotto()
tickets.reveal()





