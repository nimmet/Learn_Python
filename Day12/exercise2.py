

def passChecker(passwd):
    letters = [True for i in passwd if i.isdigit()]
    upper = [True for i in passwd if i.isupper()]
    
    if len(passwd)>8 and any(letters) and any(upper):
        print("Strong password")
    else:
        print("Weak password")
        

passwd = input("Enter your password: ")

passChecker(passwd)