
enemies = 1

def increment_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    
increment_enemies()
print(f"enemies outside function: {enemies}")

def increment_enemies(enemies):
    enemies += 2
    print(f"enemies inside function with parameter: {enemies}")
    return enemies

enemies = increment_enemies(enemies)
print(f"enemies outside function with parameter: {enemies}")
    
