import random

def roll():
    return random.randint(1, 6)

print(roll())

i = 0
while i < 100:
    print(roll())
    i = i + 1
print("Hello World")

# return user parameters
# roll a random d6
# take input for number of dice
# take input for size of dice
# have different default inputs