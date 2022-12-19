
student_scores = {
    "Harry":81,
    "Ron":79,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}

student_grades = {}

def show_grade(grades):
    for k,v in grades.items():
        print(f"{k} : {v}")

for k,v in student_scores.items():
    if v >=91 and v <=100:
        student_grades[k]="Outstanding"
    elif v >=81 and v <=90:
        student_grades[k]="Exceeds Expectations"
    elif v >=71 and v <=80:
        student_grades[k]="Acceptable"
    else:
        student_grades[k]="Fail"


show_grade(student_grades)