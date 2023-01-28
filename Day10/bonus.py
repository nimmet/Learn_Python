

try:
    w = float(input("Enter rectangle width:"))
    l = float(input("Enter rectangle length:"))
    
    if w == l:
        print("please enter different values for width and length.")
    else:
        area = w*l 
        print(area)
        
except ValueError:
    print("Please enter a number.")
