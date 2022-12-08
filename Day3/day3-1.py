
number = int(input("Which number do you want to check? "))

quit = False

while not quit:
    if number % 2 == 0:
        print("This is a an even number")
    else:
        print("This is an odd number")
    
    answer = input("Do you want to continue checking? y or n ")
    if answer == 'y':
        number = int(input("Which number do you want to check? "))
    else:
        quit = True
        