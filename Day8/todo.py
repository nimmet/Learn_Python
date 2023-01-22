import os
# todos = []

while True:
    
    action = input("\nType add, show, edit, clear, complete or exit: ").strip()
    
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
            with open('todo.txt', 'a') as file:
                file.writelines(todo.title())
            
        case "show" | "display":
            with open('todo.txt', 'r') as file:
                todos = file.readlines()
            
            # for index,item in enumerate(todos):
            #     todos[index] = item.strip("\n")
            
            todos = [item.strip("\n") for item in todos]
            
            for i in range(len(todos)):
                print(f"{i+1} - {todos[i]}")
            
            
        case "edit":
            with open('todo.txt', 'r') as file:
                todos = file.readlines()
            
            num = int(input("Number of the todo to edit:"))
            new_todo = input("Enter new todo: ")
            todos[num-1]=new_todo.title()+"\n"
            with open('todo.txt','w') as file:
                file.writelines(todos)
            
            
        case "complete":
            num = int(input("\nNumber of the todo to complete: "))
            todos.pop(num-1)
            
        case "exit":
            break
        
        case "clear":
            os.system("cls")
        
        case _:
            print("Please just enter the command offered")
print("Bye!")
        
    