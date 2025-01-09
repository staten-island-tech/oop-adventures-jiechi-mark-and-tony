import random
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