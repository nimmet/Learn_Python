import string
import random

alphabets  = string.ascii_letters
symbols = string.printable[len(string.ascii_letters)+10:]
numbers = string.printable[0:10]

print("Welcome to the PyPassword Generator!")
letter_len = int(input("How many letters would you like in your password? "))
sym_len = int(input("How many symbols would you like? "))
num_len = int(input("How many numbers would you like? "))

password = []

for i in range(letter_len):
    password.append(random.choice(alphabets))

for i in range(sym_len):
    password.append(random.choice(symbols))
    
for i in range(num_len):
    password.append(random.choice(numbers))
    
password = "".join(password)

print(f"Here is your password: {password}")

    
    


    