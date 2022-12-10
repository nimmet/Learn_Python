

nums = ["O","\\","|","/","\\","/"]
one = "O"
two = "\\"
three = "|"
four ="/"
five = "\\"
six = "/"
word ="east turkistan"
word_list = list(word)

letters = [' - ' for i in range(len(word_list))]
# for i in range(len(word)):
#     letters[i]=' - '

print(letters)
    
guess=""

if len(letters) !=0:
    print("Welcome to the Hangman game\n")
    guess= input("Guess a letter: ")
    print("\n\n\t"+' - '*len(word)+"\n\n\n")
    
    

if guess in list(word):
    for i in list(word):
        if guess == i:
            index = word_list.index(i)
            letters[index]= guess
            
    for i in letters:
        print(i,end=" ")
        
        
        
        
print("\n\n\n")



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



