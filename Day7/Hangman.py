

fails = [""," "," "," "," "," "," "]
one = "O"
two = "\\"
three = "|"
four ="/"
five = "\\"
six = "/"
word ="eastturkistan"
word_list = list(word)


letters = [' - ' for i in range(len(word_list))]

run = True

word_index =[]



print(letters)
    
guess=""
count = 0
guess_num = 0

while run:

    # if len(letters) !=0:
    #     print("Welcome to the Hangman game\n")
    #     guess= input("Guess a letter: ")
    #     # print("\n\n\t"+' - '*len(word)+"\n\n\n")
    
    print("Welcome to the Hangman game\n")
    guess= input("Guess a letter: ")

    if guess in list(word):
        
        for index, value in enumerate(list(word)):
            if guess == value:
                letters[index]= guess
                guess_num += 1
                
                if guess_num == len(word_list):
                    print("\n\nYou Win!")
                    run = False
                    
            

        for i in letters:
            print(i,end=" ")
    else:
        count +=1
        print(f"{guess} is not in the word")

     
    if guess_num == len(word_list):
        print("\nYou Win!")   
    if count == 6:
        run = False
        print("You Lose!")
        
    if count == 1:
        fails[count] = one
    elif count == 2:
        fails[count] = two
    elif count == 3:
        fails[count] = three
    elif count == 4:
        fails[count] = four
    elif count == 5:
        fails[count] = five
    else:
        fails[count] = six
            
        
        
    print("\n\n\n")



    print("   +--------------------+")
    print("   |                    |")
    print("   |                    |")
    print("   |                    |")
    print("   |                    |")
    print(f"   |                    {fails[1]}")
    print(f"   |                   {fails[4]}{fails[3]}{fails[2]}")
    print(f"   |                   {fails[6]} {fails[5]}") 
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("================================")



