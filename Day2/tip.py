
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))/100
total = bill * tip + bill

print(f"The total bill is ${round(total,2)} and each person should pay ${round(float(total/people),2)}")