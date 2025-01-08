import random
"""numbers = list(range(1,71))
class Ticket():
    def __init__(self, guesses=5):
        self.guesses = guesses
        self.guess = []
        self.random_number = []
    def lotto(self):
        while True:
            try:
                self.guess = []
                for _ in range(self.guesses):
                    guessing = int(input("Choose a number from 1-70: "))  
                    if 1 <= guessing <= 70:
                        self.guess.append(guessing)
                    else:
                        print("Enter a valid input 1-70 ")
                if len(self.guess) == 5:#Chatgpt made it loop 5 times instead of 5 lines of the same code  
                    break
                else:
                    print("Please choose 5 unique numbers.")

            except ValueError:
                print("Invalid input! Please enter a valid integer.")
    def rlotto(self):
        self.random_number = [random.choice(range(1, 71)), 5]
        return self.random_number
    def reveal(self):
        if self.guess == self.random_number:
            print("win")
        else:
            print("lose")
tickets = Ticket()
tickets.rlotto()
tickets.lotto()
tickets.reveal() """
class Tickets():
    def __init__(self, guesses=5):
        self.guesses = guesses
        self.guess = []
        self.random_number = []
        self.guessing = True

    def rlotto(self):
        # Generate 5 random unique numbers
        self.random_number = random.sample(range(1, 71), self.guesses)

    def reveal(self):
        # Sort both lists for comparison (since order doesn't matter)
        if sorted(self.guess) == sorted(self.random_number):
            return True
        else:
            return False
ticket = Tickets()