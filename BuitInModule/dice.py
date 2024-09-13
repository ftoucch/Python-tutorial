import random


class Dice:
    def roll():
         firstnumber = random.randint(1,6)
         secondnumber = random.randint(1,6)
         return firstnumber, secondnumber


dice = Dice
print(dice.roll())