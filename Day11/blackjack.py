import random

playGame = False

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
y=[]
c=[]

while not playGame:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play=='n':
        print("Bye!")
        playGame = True
    
    else:
        y1 = random.randint(0, len(cards)-1)
        y2 = random.randint(0, len(cards)-1)
        c1 = random.randint(0, len(cards)-1)
        c2 = random.randint(0, len(cards)-1)
        y.append(y1)
        y.append(y2)
        c.append(c1)
        c.append(c2)
        
        print(f"Your cards: [{y1}, {y2}], current score: {y1+y2}")
        print(f"Computer's first card: {c1}")
        anothor = input("Type 'y' to get another card, type 'n' to pass: ")
        if anothor=='y':
            y.append(cards[random.randint(0,len(cards)-1)])
            print(f"    Your cards: {y}, current score: {sum(y)}")
            print(f"    Computer's first card: {c[0]}")
            print(f"    Your final hand: {y}, final score: {sum(y)}")
            print(f"    Computer's final hand: {c}, final score: {sum(c)}")
            
            if sum(y) == 21:
                print("You Win 🏆")
            elif sum(c) == 21:
                print("You went over. You lose 😭")     
            elif sum(y) > sum(c):
                print("You went over. You lose 😭")
            else:
                print("You Win 🏆")
        
        
    