import random
import os

class ticket():
    def lotto():
        guess = [input("Choose a number from 1-70: ") for _ in range(5)] #Chatgpt made it loop 5 times instead of 5 lines of the same code
        return tuple(guess)
    def rlotto():
        numbers = list(range(1,71))    
        random_number = [random.choice(numbers) for _ in range(5)]
        print(random_number)
        return random_number
    def reveal():
        for i in guessing:
            if i == real:
                print("cool")
            elif i != real:
                print("lose")
real = ticket.rlotto()
guessing = ticket.lotto()

show = ticket.reveal()





