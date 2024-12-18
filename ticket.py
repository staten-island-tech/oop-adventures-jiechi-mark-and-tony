import random


class ticket():
    def __init__(self):
        self.guess = []
        self.random_number = []
    def lotto(self):
        self.guess = [int(input("Choose a number from 1-70: ")) for _ in range(5)] #Chatgpt made it loop 5 times instead of 5 lines of the same code
        if 1 <= self.guess <= 70:
            return self.guess
        else:
            print("Enter a valid number")
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


"""         except ValueError:
            print("Invalid input. Please enter a valid integer.") """
