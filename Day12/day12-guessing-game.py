import random

print("Welcome to the number guessing game!")

print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
attemp = 0
tried = 0
guess=0
diff = 0
number = random.randint(1,100)
if difficulty == "hard":
    diff=5
    attemp = 5
else:
    diff=10
    attemp = 10
    
while (tried < diff):
    print(f"You have {attemp} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.")
        print("Guess again.")
        tried += 1
        attemp -= 1
    elif guess < number:
        print("Too low.")
        print("Guess again.")
        tried += 1
        attemp -= 1
    else:
        print("You win")
        
    
    
        
