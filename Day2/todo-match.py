import os


todo =""
todos = []
decition=""
quit=False 

while not quit:
    decition = input("Type what to do (add,show,clear,exit):")
    
    match decition:
        case "add":
            todo = input("Add a todo item: ")
            todos.append(todo)
        case "show":
            for i in range(len(todos)):
                print(f"{i+1} - {todos[i].capitalize()}")
        case "clear":
            os.system('cls')
        case "exit":
            quit = True
            