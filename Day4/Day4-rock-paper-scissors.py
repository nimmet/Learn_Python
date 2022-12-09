import random

game = ["👊","✋","✂"]
choice2 = random.choice(game)
choice1 = game[int(input("What do you choice? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))]

print(choice1)
print("Computer Chose:")
print(choice2)

if choice1 == game[0] and choice2 == game[1]:
    print("You lose!")
elif choice1 == game[0] and choice2 == game[2]:
    print("You win!")
elif choice1 == game[1] and choice2 == game[0]:
    print("You Win!")
elif choice1 == game[1] and choice2 == game[2]:
    print("You lose!")
elif choice1 == game[2] and choice2 == game[0]:
    print("You lose!")
elif choice1 == game[2] and choice2 == game[1]:
    print("You Win!")
else:
    print("Drawn!")
