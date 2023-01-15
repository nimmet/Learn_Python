
todo =""
quit=""
count=0
todos=[]

while quit != "y":
    todo = input("Enter a todo: ")
    if todo !="y": 
        todos.append(todo.capitalize())
    else:
        quit ="y"
    
    for i in range(len(todos)):
        print(f"{i+1} - {todos[i]}")
    
