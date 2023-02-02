import random

def randNumGenerator(lower, upper):
    num = random.randint(lower, upper)
    return num


lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

print(randNumGenerator(lower, upper))