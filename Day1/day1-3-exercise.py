
name = input("What is your name?")
name = name.capitalize()
print(f'Hello {name}, you name is {len(name)} characters long')

first,last = input("What is your full name?").split()
print(f'Hello {first.capitalize()}, you full name is {first.capitalize()+" "+last.capitalize()}.')

numbers = input("enter three numbers: ").split()
print(numbers)

a  = input("a: ")
b  = input("b: ")

print(f" a: {a}, b: {b}")

a,b = b,a 

print(f"after changing place a: {a}, b: {b}")