import string



str = list("hello world!")

test = ['h','e','l','l','o']
# ,'w','o','r','l','d','z'

encode = []
decode = []

print("Welcome to Caesar Cipher!")
stopEncode = False



while not stopEncode:
    coding = input("Type \'encode\' to encrypt, type \'decode\' to decrypt: ")
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    alpha = list(string.ascii_lowercase)
    cipher = list(alpha[shift:]+alpha[0:shift])
    
    if coding == "encode":

        for j in list(message): 
            
            for i,v in enumerate(alpha):
                if j == v:
                    encode.append(cipher[i])
                
                    
            if not j.isalpha():
                encode.append(j)
        
        print(f'Here is the encoded result: {"".join(encode)}')
        again = input("Type \'yes\' if you want to go again. Otherwise type \'no\':")
        if  again == 'no':
            stopEncode=True
        else:
            encode.clear()
    else:
        for j in list(message): 
            
            for i,v in enumerate(cipher):
                if j == v:
                    decode.append(alpha[i])
                
                    
            if not j.isalpha():
                decode.append(j)
        
        print(f'Here is the decoded result: {"".join(decode)}')
        again = input("Type \'yes\' if you want to go again. Otherwise type \'no\':")
        if  again == 'no':
            stopEncode=True
        else:
            decode.clear()
        
        
        
    
           
    
           
        
            
            


# print(string.ascii_lowercase)
# print(string.ascii_lowercase[9:]+string.ascii_lowercase[0:9])