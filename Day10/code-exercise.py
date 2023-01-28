# Percentage calculator

while True:
    
    try:
        total = int(input("Enter total value: "))
        val = int(input("Enter value: "))
        
        if not str(val).isdigit():
            raise ValueError

        if total == 0:
            print("You total value cannot be zero.")
        else:
            print(f"That is {(val*100/total):.2f}%")
        
        
    except ValueError:
        print("Please just enter a number.")
        continue
    