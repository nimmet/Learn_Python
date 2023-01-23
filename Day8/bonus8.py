

date = input("Enter today's date: ")
mood = int(input("Hod do you rate your mood today from 1 to 10? "))


thought=input("Let your thoughts flow: ")

with open(f"{date+'.txt'}","w") as file:
    file.writelines("Date: " + date)
    file.writelines(f"\nMode: {mood}")
    file.writelines("\nThought: "+thought)

    