
def waterState(temp):
    if temp>0 and temp<100:
        return "Liquid"
    elif temp <=0:
        return "Sold"
    else:
        return "Gas"
    
    
    
temperature = int(input("Enter water temperature: "))
print(waterState(temperature))