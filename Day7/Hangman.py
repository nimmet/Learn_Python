

nums = ["O","\\","|","/","\\","/"]
one = "O"
two = "\\"
three = "|"
four ="/"
five = "\\"
six = "/"
word ="East Turkistan"

letters =[]
guess=""

if len(letters)==0:
    print("Welcome to the Hangman game\n")
    guess= input("Guess a letter: ")
    print("\n\n\t"+' - '*len(word)+"\n\n\n")
    
    
else:
    for i in range(0, len(letters)):
        if guess in list(word):
            print("It is here")
        
        




print("   +--------------------+")
print("   |                    |")
print("   |                    |")
print("   |                    |")
print("   |                    |")
print(f"   |                    {one}")
print(f"   |                   {four}{three}{two}")
print(f"   |                   {six} {five}") 
print("   |")
print("   |")
print("   |")
print("   |")
print("   |")
print("   |")
print("   |")
print("   |")
print("================================")



