
feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    feet,inches = feet_inches.split()
    feet = float(feet)
    inches = float(inches)
    
    meters = feet * 0.3048 + inches * 0.0254
    # return f"{feet} feet and {inches} inches is equal to {meters:.2f} meters"
    return meters

result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slider.")