import random

def roll(size):
    return random.randint(1, size)

print("A d6")
print(roll(6))

print("A d8")
print(roll(8))

print("A d10")
print(roll(10))

def roll_many(number):
    i = 0
    while i < number:
        print(roll(6))
        i = i + 1
    return "done"

print("Rolling 20 dice")
roll_many(20)

# return user parameters
# roll a random d6
# take input for number of dice
# take input for size of dice
# have different default inputs