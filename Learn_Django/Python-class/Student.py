
class Student():
    
    faculty = "CS" # Class Object attribute
    
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        


st1 = Student('Nimmet',4)

st2 = Student("Uyghur",3.7)


print(st1.name)
print(st1.faculty)

        