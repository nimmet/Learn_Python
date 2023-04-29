
class Person():
    
    def __init__(self,first,last):
        
        self.first = first
        self.last = last
        
    
    def hello(self):
        print("Hello")
        
    
    def report(self):
        print(f"I am {self.first} {self.last}")
        



class Agent(Person):
    
    def __init__(self,first,last,code_name):
        Person.__init__(self,first,last)
        self.code_name = code_name
        
        
    def reveal(self,passcode):
        if passcode == 123:
            print(f"I am a secret agent, my code name is {self.code_name}")
        else:
            self.report()



p = Person("John","Smith")
p.hello()
p.report()

p1 = Agent("Alen","Turing","CS")
p1.reveal(123)