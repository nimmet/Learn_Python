

passwd = input("Enter new password: ")

digit = [i.isdigit() for i in passwd]
digit= True in digit
upper = [i.isupper() for i in passwd]
upper = True in upper
special = [i.isprintable() for i in passwd]
special = True in special



if len(passwd) >= 8 and digit and upper and special:
    print("Great password there")
elif len(passwd) >= 8 and digit and upper == False:
    print("Password is ok, but not too strong")
else:
    print("Weak password")