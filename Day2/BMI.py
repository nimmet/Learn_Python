height = float(input("enter you height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height**2,2)

print(f"Your BMI index is {bmi}.")