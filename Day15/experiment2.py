import csv

with open("weather.csv",'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city name: ").title()

for row in data:
    for r in row:
        if r == city:
            print(f"City: {row[0]}, Temperature: {row[1]}")