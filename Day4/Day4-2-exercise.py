from random import choice

# people = ["Angela","Ben", "John", "Jenny","Michael","Chloe"]
people = input("Give me everybody's names seperated by a comma: ")
people=people.split(",")

print(people)
print(f"{choice(people)} is going to buy the meal today!")