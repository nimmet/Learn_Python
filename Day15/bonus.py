import csv

answer=0
with open("quiz.csv") as file:
    data = list(csv.reader(file))
    
    for d in data:
        c=1
        
        print(d[0])
        for i in len(d):
            print(f"{i+1}-{d[i]}")
            c += 1

print(data)
            