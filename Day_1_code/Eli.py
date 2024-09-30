/.;'/.import random

# placeholder value
dice1 = 1
dice2 = 0
dice3 = 2

counter = 0
while dice1 != dice2 or dice1 != dice3:
    counter += 1

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
   
    print(dice1,dice2,dice3)

print("ROLLED THE SAME DICE", counter, "times")
