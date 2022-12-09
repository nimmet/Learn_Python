import random

random_integer = []
random_float = []

for i in range(10):
    random_integer.append(random.randint(0,100))
    
print("Our integer random numbers: ")
print(random_integer)

for i in range(10):
    random_float.append(round(random.random(),2))
    
print("Our float random numbers: ")
print(random_float)

