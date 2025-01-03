import random
numbers = list(range(1,71))
class ticket():
    def __init__(self, guesses=5):
        self.guesses = guesses
        self.guess = []
        self.random_number = []
    def lotto(self):
        while True:
            try:
                self.guess = []
                for _ in range(self.guesses):
                    guessing = int(input("Choose a number from 1-70: ")) #Chatgpt made it loop 5 times instead of 5 lines of the same code   
                    if 1 <= guessing <= 70:
                        self.guess.append(guessing)
                    else:
                        print("Enter a valid input 1-70 ")
                if len(self.guess) == 5:
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
tickets = ticket()
tickets.rlotto()
tickets.lotto()
tickets.reveal()


