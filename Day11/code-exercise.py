
def get_max():
    grades =[9.6,9.2,9.7]
    mx = 0
    m = 0
    for i in grades:
        if i > mx:
            mx=i
        else:
            m=i
    print(f"Max: {mx}, Min: {m}")
    
def get_mx():
    grades =[9.6,9.2,9.7]
    print(f"Max: {max(grades)}, Min: {min(grades)}" )
    
    

get_max()
get_mx()

