quit =""
result=0


def calculate():
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
    return result

def calculateWithResult(result):
    
    for i in ["+","-","*","/"]:
            print(i)
        
    operator=input("Pick an operator: ")
    second = int(input("What is the second number?: "))
    
    if operator == "+":
        result=result+second
        print(f"{result} {operator} {second} = {result}")
    elif operator == "-":
        result=result-second
        print(f"{result} {operator} {second} = {result}")
    elif operator == "*":
        result=result*second
        print(f"{result} {operator} {second} = {result}")
    else:
        result=round(result/second,2)
        print(f"{result} {operator} {second} = {result}")
    return result
    
    

while quit !="q":
    result=calculate() 
    again = input("Do you want to continue with this result? y,n or q for quit: ")

    
    
    
    
    if again == "y":
        # first = int(input("What is the first number?: "))
        result = calculateWithResult(result)
            
        again = input("Do you want to continue with this result? y,n or q for quit: ")
    
    elif again=='n':
        result=calculate()
        again = input("Do you want to continue with this result? y,n or q for quit: ") 
        result = calculateWithResult(result)
    else:
        print("Thank very much for using this calculator!")
        quit="q"       
    


        
    
    