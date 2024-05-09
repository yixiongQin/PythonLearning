import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members = ['John', 'Doe', 'Jane']

leader = random.choice(members)
print(leader)

class Dice:
    def roll(self):
        return random.randint(1, 6)

dice = Dice()
print(dice.roll()) 