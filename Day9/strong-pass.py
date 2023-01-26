

passwd = input("Enter new password: ")

digit = [True for i in passwd if i.isdigit() ]
digit= any(digit)
upper = [True for i in passwd if i.isupper()]
upper = any(upper)
special = [True for i in passwd if i.isprintable()]
special = any(special)


if len(passwd) >= 6 and all([digit,upper,special]):
    print("Great password there")
elif len(passwd) >= 6 and digit and upper == False:
    print("Password is ok, but not too strong")
elif len(passwd) >= 6:
    print("Password is ok, but not too strong")
    
else:
    print("Weak password")