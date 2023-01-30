# Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter.

def convertToCubic(liter):
    return round(liter/1000,2)


liter = float(input("Enter liter: "))

print(f"{liter} liters is equal to {convertToCubic(liter)} cubic meters.")
