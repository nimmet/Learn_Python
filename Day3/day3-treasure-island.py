print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("left or right? ").lower()


if direction == "right":
    print("Game Over!")
else:
    action=input("swim or wait?").lower()
    if action == "swim":
        print("Game Over!")
    else:
        door = input("Which door?").lower()
        if door == "blue":
            print("Game Over!")
        elif door == "red":
            print("Game Over!")
        else:
            print("You Win!")
            