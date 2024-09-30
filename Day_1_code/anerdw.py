"""
Simulate dice rolls. Will roll three dice repeatedly unti all three come up the
same number, then stop.
"""

import random

die1: int = 0
die2: int = 1
die3: int = 2
counter: int = 0

while not die1 == die2 == die3:
    counter += 1

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)

    print(die1, die2, die3)

print(f"Rolled {die1} thrice! It took {counter} rolls.")
