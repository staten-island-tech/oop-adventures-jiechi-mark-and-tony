import random
import os
class ticket():
    def lotto(self):
        n1 = input("Choose a number from 1-70: ")
        n2 = input("Choose a number from 1-70: ")
        n3 = input("Choose a number from 1-70: ")
        n4 = input("Choose a number from 1-70: ")
        n5 = input("Choose a number from 1-70: ")
        return (n1, n2, n3, n4, n5)
Lotto = ticket()
Lotto.lotto()
