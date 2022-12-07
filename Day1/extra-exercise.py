from random import *

list = [1,2,3,4,5,6,7,8,9]

print(f'My random choice is: {choice(list)}')

num = []

for i in range(10):
    num.append(randint(0,11))
    
print("Randomly generated number: ",num)

for i in range(10,0,-1):
    print(i, end=' ')