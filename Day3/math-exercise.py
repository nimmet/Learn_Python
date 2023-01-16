import os
todos = []

while True:
    
    action = input("Type add, clear, show or exit: ").strip()
    
    match action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.title())
        case 'show' | 'display':
            for i in range(len(todos)):
                print(f"{i+1} - {todos[i]}")
        
        case 'clear':
            os.system('cls')
            
        case 'exit':
            break      
        case _:
            print("You entered something out of the command list!")
        
print("Bye!")