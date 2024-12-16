import random

class ticket():
    def lotto():
        guess = [input("Choose a number from 1-70: ") for _ in range(5)] #Chatgpt made it loop 5 times instead of 5 lines of the same code
        return guess
    def rlotto():
        numbers = list(range(1,71))    
        random_number = [random.choice(numbers) for _ in range(5)]
        print(random_number)
        return random_number
    def reveal():
        if guess == real:
            print("win")
        elif guess != real:
            print("lose")
real = ticket.rlotto()
guess = ticket.lotto()
show = ticket.reveal()





