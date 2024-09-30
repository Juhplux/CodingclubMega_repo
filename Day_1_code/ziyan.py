import random
dice1=0
dice2=1

counter=0

while dice1 != dice2:
    counter += 1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print(dice1, dice2)

print ("rolled the same dice after", counter)
