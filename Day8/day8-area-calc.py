
h = int(input("Hight of wall: "))
w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height=h, width=w, coverage= coverage):
    can=(h*w)/coverage
    print(f"You will need {round(can)} cans of paint.")
    
paint_calc(h,w,coverage)