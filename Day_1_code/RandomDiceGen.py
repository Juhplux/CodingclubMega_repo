import random

dice1 = 0
dice2 = 0
dice3 = 0
counter = 0
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)

while not dice1 == dice2 == dice3:
    counter+=1
    dice1=random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    print(dice1, dice2, dice3)

print("Rolled the same dice ", counter, "Times")
