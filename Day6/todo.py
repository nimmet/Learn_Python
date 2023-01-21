import os
# todos = []

while True:
    
    action = input("Type add, show, edit, clear, complete or exit: ").strip()
    
    match action:
        
        # case "file":
        #     todo = input("Enter a todo from a file: ")
        #     file = open('todo.txt', 'r')
        #     todo = file.readline()
        #     file.close()
        #     todos.append(todo.title())
            
            
        case "add":
            todo = input("Enter a todo: ")+"\n"
            # todos.append(todo.title())
            file = open('todo.txt', 'a')
            file.writelines(todo.title())
            
        case "show" | "display":
            file = open('todo.txt', 'r')
            todos = file.readlines()
            for i in range(len(todos)):
                print(f"{i+1} - {todos[i]}")
            file.close()
            
        case "edit":
            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()
            num = int(input("Number of the todo to edit:"))
            new_todo = input("Enter new todo: ")
            todos[num-1]=new_todo.title()
            file = open('todo.txt','w')
            file.writelines(todos)
            file.close()
            
        case "complete":
            num = int(input("Number of the todo to complete: "))
            todos.pop(num-1)
            
        case "exit":
            break
        
        case "clear":
            os.system("cls")
        
        case _:
            print("Please just enter the command offered")
print("Bye!")
        
    