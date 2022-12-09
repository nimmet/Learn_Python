row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

poision = input("Where do you want to put the treasure?")
p1,p2 = int(poision[0]),int(poision[1])
map[p1-1][p2-1] = "💰"

print(f"{row1}\n{row2}\n{row3}")

