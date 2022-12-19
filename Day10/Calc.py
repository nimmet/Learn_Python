quit =""
result=0
again=""

while quit !="q":
    first = int(input("What is the first number?: "))
    for i in ["+","-","*","/"]:
        print(i)
    
    operator=input("Pick an operator: ")
    second = int(input("What is the second number?: "))
    
    if operator == "+":
        result=first+second
        print(f"{first} {operator} {second} = {result}")
    elif operator == "-":
        result=first-second
        print(f"{first} {operator} {second} = {result}")
    elif operator == "*":
        result=first*second
        print(f"{first} {operator} {second} = {result}")
    else:
        result=round(first/second,2)
        print(f"{first} {operator} {second} = {result}")
    
    if again == "y":
        first = int(input("What is the first number?: "))
        for i in ["+","-","*","/"]:
            print(i)
        
        operator=input("Pick an operator: ")
        second = int(input("What is the second number?: "))
        
        if operator == "+":
            result=first+second
            print(f"{first} {operator} {second} = {result}")
        elif operator == "-":
            result=first-second
            print(f"{first} {operator} {second} = {result}")
        elif operator == "*":
            result=first*second
            print(f"{first} {operator} {second} = {result}")
        else:
            result=round(first/second,2)
            print(f"{first} {operator} {second} = {result}")
            
    


        
    
    