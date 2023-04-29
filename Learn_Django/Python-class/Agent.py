

class Agent():
    
    origin="Uyghuristan"
    
    def __init__(self,name,height,weight):
        
        self.height = height
        self.weight = weight
        self.name = name
        
    def __str__(self):
        return f"Agent Name: {self.name}, Origin: {self.origin}, Height: {self.height}, Weight: {self.weight}"
        

x = Agent("Uyghur",170,90)

print(x)

