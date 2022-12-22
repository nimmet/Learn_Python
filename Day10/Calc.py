quit =""
result=0
again=""


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
    again = input(f"Type 'y' to continue calculating with {result} or \ntype 'n' to start a new calculation or \ntype 'q' to quit: ")
    if again == 'q':
            print("Thank very much for using this calculator!")
            quit="q"
    
    
    
    
    while again == "y":
        # first = int(input("What is the first number?: "))
        
        result = calculateWithResult(result)
        again = input(f"Type 'y' to continue calculating with {result} or \ntype 'n' to start a new calculation or \ntype 'q' to quit: ")
        if again == 'q':
            print("Thank very much for using this calculator!")
            quit="q"
    
    while again =='n':
        result=calculate()
        again = input(f"Type 'y' to continue calculating with {result} or \ntype 'n' to start a new calculation or \ntype 'q' to quit: ")
        result = calculateWithResult(result)
        again = input(f"Type 'y' to continue calculating with {result} or \ntype 'n' to start a new calculation or \ntype 'q' to quit: ")

        
        if again == 'q':
            print("Thank very much for using this calculator!")
            quit="q"       
    


        
    
    