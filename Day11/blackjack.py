import random

playGame = False

carts = [11,2,3,4,5,6,7,8,9,10,10,10,10]

while not playGame:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play=='n':
        print("Bye!")
        playGame = True
    
    else:
        y1 = random.randint(0, len(carts)-1)
        y2 = random.randint(0, len(carts)-1)
        c1 = random.randint(0, len(carts)-1)
        c2 = random.randint(0, len(carts)-1)
        print(y1,y2,c1,c2)
    