
even_nums = []

for i in range(1,101):
    if i % 2 == 0:
        even_nums.append(i)

print(even_nums)
print(f"The sum of the even numbers between 0 and 100 is {sum(even_nums)}")