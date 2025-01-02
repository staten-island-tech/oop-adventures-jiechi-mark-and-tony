import random
numbers = list(range(1,71))
class ticket():
    def __init__(self, guesses=5):
        self.guesses = guesses
        self.guess = []
        self.random_number = []
    def lotto(self):
        self.guess = [int(input("Choose a number from 1-70: ")) for _ in range(5)] #Chatgpt made it loop 5 times instead of 5 lines of the same code   
        while True:
            try:
                if 1 <= self.guess <= 70:
                    return self.guess
                else:
                    print("Enter a valid input 1-70: ")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
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

""" class NumberGuesser:
    def __init__(self, total_guesses=5):
        self.total_guesses = total_guesses  # Number of guesses the user should make
        self.guesses = []  # List to store valid guesses

    def get_valid_input(self):
        """Prompts the user for a valid input (integer between 1 and 70)."""
        while True:
            try:
                user_input = int(input("Choose a number from 1-70: "))
                if 1 <= user_input <= 70:
                    return user_input
                else:
                    print("Please enter a number between 1 and 70.")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    def collect_guesses(self):
        """Collects the specified number of valid guesses."""
        for _ in range(self.total_guesses):
            guess = self.get_valid_input()  # Get valid input from the user
            self.guesses.append(guess)  # Append the guess to the list """


