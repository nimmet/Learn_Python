import string

alpha = list(string.ascii_lowercase)
cipher = list(alpha[9:]+alpha[0:9])

str = list("hello world!")

test = ['h','e','l','l','o']
# ,'w','o','r','l','d','z'
shift = 9
encode = []

print(str)
for j in str: 
    for i,v in enumerate(alpha):
        if j == v:
            encode.append(cipher[i])
            print(cipher[i],end='')
        
        
            
    if j == ' ':
        encode.append(' ')
           
    
           
        
            
            

print(encode)
print(string.ascii_lowercase)
print(string.ascii_lowercase[9:]+string.ascii_lowercase[0:9])