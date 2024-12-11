import random
import os

class ticket():
    def lotto():
        number = [input("Choose a number from 1-70: ") for _ in range(5)]
        return tuple(number)
    def rlotto():
        numbers = list(range(1,71))    
        random_number = [random.choice(numbers) for _ in range(5)]
        print(random_number)
    def reveal(number, random_number):
        for i in number:
            if i == random_number:
                print("cool")
            elif i != random_number:
                print("lose")
    lotto()





