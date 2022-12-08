
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
names = name1+name2
true = 0
love = 0
# 
for i in ["t","r","u","e"]:
    true += names.count(i)
    
for i in ["l","o","v","e"]:
    love += names.count(i)
    
score = int(str(f"{true}{love}"))

if score < 10 or score > 90:
    print(f"Your score is: {score}, you go together like coke and mentos")
elif score > 40 and score <50:
    print(f"Your score is: {score}, you are alright together.")
else:
    print(f"Your score is: {score}")


    