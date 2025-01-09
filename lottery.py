import random
class Tickets():
    def __init__(self, guesses=5, balance = 1000):
        self.guesses = guesses
        self.guess = []
        self.random_number = []
        self.guessing = True
        self.balance = balance

    def rlotto(self):
        # Generate 5 random unique numbers
        self.random_number = random.sample(range(1, 71), self.guesses)

    def reveal(self):
        # Sort both lists for comparison (since order doesn't matter)
        if sorted(self.guess) == sorted(self.random_number):
            self.balance += 100000
            return True
        else:
            self.balance -= 10
            return False
ticket = Tickets()