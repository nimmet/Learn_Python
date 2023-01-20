import os
todos = []

while True:
    
    action = input("Type add, show, edit, clear, file, complete or exit: ").strip()
    
    match action:
        
        case "file":
            todo = input("Enter a todo from a file: ")+"\n"
            file = open('todo.txt', 'r')
            todo = file.readline()
            file.close()
            todos.append(todo.title())
            
            file = open('todo.txt', 'a')
            file.writelines("\n"+todo)
            file.close()
            
            
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.title())
            file = open('todo.txt', 'a')
            file.writelines("\n"+todo)
            
        case "show" | "display":
            file = open('todo.txt', 'r')
            todos = file.readlines()
            for i in range(len(todos)):
                print(f"{i+1} - {todos[i]}")
        case "edit":
            num = int(input("Number of the todo to edit:"))
            new_todo = input("Enter new todo: ")
            todos[num-1]=new_todo.title()
            
        case "complete":
            num = int(input("Number of the todo to complete: "))
            todos.pop(num-1)
            
        case "exit":
            break
        
        case "clear":
            os.system("cls")
        
        case _:
            print("Please just enter the command offered")
        
    