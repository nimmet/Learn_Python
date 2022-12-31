
enemies = 1

def increment_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    
increment_enemies()
print(f"enemies outside function: {enemies}")
