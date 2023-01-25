

passwd = input("Enter new password: ")

digit = [i.isdigit() for i in passwd]
digit= True in digit
upper = [i.isupper() for i in passwd]
upper = True in upper

print(digit)
print(upper)

if len(passwd) >= 8 and digit and upper:
    print("Strong password")
else:
    print("Weak password")