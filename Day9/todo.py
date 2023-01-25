import os
# todos = []

while True:
    
    
    action = input("\nType add, show, edit, clear, complete or exit: ").strip()
    
    
        
        # case "file":
        #     todo = input("Enter a todo from a file: ")
        #     file = open('todo.txt', 'r')
        #     todo = file.readline()
        #     file.close()
        #     todos.append(todo.title())
            
            
    if "add" in action or "new" in action or "more" in action:
        
        # todos.append(todo.title())
        # todo = action.replace("add","").strip()
        todo = action[4:]
        
        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        
        todos.append("\n"+todo.title().strip())
    
        with open('todo.txt', 'w') as file:
            file.writelines(todos)
    # else:
    #     todo = input("Enter a todo: ")+"\n"
            
        
    elif "show" in action:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        
        # for index,item in enumerate(todos):
        #     todos[index] = item.strip("\n")
        
        todos = [item.strip("\n") for item in todos]
        
        for i in range(len(todos)):
            print(f"{i+1} - {todos[i]}")
            
    elif "display" in action:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        
        # for index,item in enumerate(todos):
        #     todos[index] = item.strip("\n")
        
        todos = [item.strip("\n") for item in todos]
        
        for i in range(len(todos)):
            print(f"{i+1} - {todos[i]}")
        
        
    elif "edit" in action:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        
        
        # num = int(input("Number of the todo to edit:"))
        num = int(action[5:])
        new_todo = input("Enter new todo: ")
        todos[num-1]=new_todo.title()+"\n"
        with open('todo.txt','w') as file:
            file.writelines(todos)
        
        
    elif "complete" in action:
        # num = int(input("\nNumber of the todo to complete: "))
        num = int(action[len("complete"):])
        
        with open('todo.txt', 'r') as file:
            todos = file.readline()
        
        todos = [item.strip("\n") for item in todos] 
               
        todos.pop(num-1)
        
        with open('todo.txt', 'w') as file:
            file.writelines(todos)
            
        
    elif "exit" in action:
        break
    
    elif "clear" in action:
        os.system("cls")
    
    else:
        print("Command is not valid.")
    
    # case _:
    #     print("Please just enter the command offered")
print("Bye!")
        
    