
def calAge(yob,current_year=2023):
    return current_year - yob





yob = int(input("Enter you birth year: "))

print(f"You was born in {yob}, and now you are {calAge(yob)} years old.")
