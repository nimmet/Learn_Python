
scores = input("Input a list of scores: ").split()

for i in range(len(scores)):
    scores[i] = int(scores[i])

print(scores)
print(f"The heights score in the class is: {max(scores)}.")