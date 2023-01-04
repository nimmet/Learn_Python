person = {}

stop = False

print("Welcome to the secret auction program.")

while not stop:
    
    
    name = input("What is you name?: ")
    bit = int(input("What is you bid?: "))
    more = input("Are there any other bidders? Type 'yes' or 'no'.")
    person[name]=bit 
    
    if more == 'no':
        m=0
        n=""
        
        for k,v in person.items():
            if v> m:
                m=v
                n=k
                
            
        print(f"The winner is {n} with a bid of ${m}.")
        stop = True
    
        
        
        
        
    
    
    