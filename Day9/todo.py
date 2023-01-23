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
            
            
    if "add" in action:
        
        # todos.append(todo.title())
        todo = action.replace("add","").strip()
    
        with open('todo.txt', 'a') as file:
            file.writelines("\n"+todo.title())
    # else:
    #     todo = input("Enter a todo: ")+"\n"
            
        
    if "show" in action:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        
        # for index,item in enumerate(todos):
        #     todos[index] = item.strip("\n")
        
        todos = [item.strip("\n") for item in todos]
        
        for i in range(len(todos)):
            print(f"{i+1} - {todos[i]}")
            
    if "display" in action:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        
        # for index,item in enumerate(todos):
        #     todos[index] = item.strip("\n")
        
        todos = [item.strip("\n") for item in todos]
        
        for i in range(len(todos)):
            print(f"{i+1} - {todos[i]}")
        
        
    if "edit" in action:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        
        
        num = int(input("Number of the todo to edit:"))
        new_todo = input("Enter new todo: ")
        todos[num-1]=new_todo.title()+"\n"
        with open('todo.txt','w') as file:
            file.writelines(todos)
        
        
    if "complete" in action:
        num = int(input("\nNumber of the todo to complete: "))
        todos.pop(num-1)
        
        with open('todo.txt', 'w') as file:
            for item in todos:
                file.writelines(item+"\n")
            
        
    if "exit" in action:
        break
    
    if "clear" in action:
        os.system("cls")
    
    # case _:
    #     print("Please just enter the command offered")
print("Bye!")
        
    