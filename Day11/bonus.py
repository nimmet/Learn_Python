

def get_average(filename):
    sm=0
    with open(filename, 'r') as file:
        data = file.readlines()[1:] # to get read of first line
    
    for i in data:
        sm += float(i)
    
    print(f"The average is {round(sm/len(data),2)}")
            
def get_avg(filename):
    count = 0
    sm = 0
    
    with open(filename, 'r') as file:
        next(file)
        
        for line in file:
            sm += float(line)
            count += 1
            
    return round(sm/count,2)  

print(get_avg('data.txt'))   

get_average('data.txt')  
    
            