
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2,2)

if bmi < 18.5:
    print("underwait")
elif bmi > 18.5 and bmi < 25:
    print("normal weight")
elif bmi > 25 and bmi < 30:
    print("overweight")
elif bmi > 30 and bmi < 35:
    print("obese")
else:
    print("clinically obese")
