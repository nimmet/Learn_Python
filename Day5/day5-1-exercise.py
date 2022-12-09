heights = input("Input a list of student heights ").split()

total = 0

for i in range(len(heights)):
    heights[i] = int(heights[i])
    total += heights[i]

print(heights[i])

print(f"There are totally {len(heights)} students and average heights: {round(total/len(heights),2)} CM.")