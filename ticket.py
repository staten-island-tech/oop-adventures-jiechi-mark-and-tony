import random
numbers = list(range(1,71))
class ticket():
    def __init__(self):
        self.guess = []
        self.random_number = []
    def lotto(self):
        while True:
            try:
                self.guess = [int(input("Choose a number from 1-70: ")) for _ in range(5)] #Chatgpt made it loop 5 times instead of 5 lines of the same code      
                if self.guess not in numbers:
                    print("Please choose a number between 1 and 70: ")
            except ValueError:
                print("Invalid value, enter an integer: ")
                return self.guess
    def rlotto(self):
        self.random_number = [random.choice(range(1, 71)) for _ in range(5)]
        return self.random_number
    def reveal(self):
        if self.guess == self.random_number:
            print("win")
        else:
            print("lose")
tickets = ticket()
tickets.rlotto()
tickets.lotto()
tickets.reveal()


