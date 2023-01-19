import os
todos = []

while True:
    
    action = input("Type add, show, edit, clear or exit: ").strip()
    
    match action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.title())
            
        case "show" | "display":
            for i in range(len(todos)):
                print(f"{i+1} - {todos[i]}")
        case "edit":
            num = int(input("Number of todo to edit:"))
            new_todo = input("Enter new todo: ")
            todos[num-1]=new_todo.title()
        case "exit":
            break
        
        case "clear":
            os.system("cls")
        
        case _:
            print("Please just enter the command offered")
        
    