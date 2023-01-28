# Percentage calculator

while True:
    
    try:
        total = int(input("Enter total value: "))
        val = int(input("Enter value: "))

        print(f"That is {(val/total):.2f}%")
        
        
    except ValueError:
        print("Please just enter a number.")
        continue
    