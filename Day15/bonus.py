import json


correct_answer=0
incorrect_answer=0


with open("quiz.json","r") as file:
    content = file.read()
    
data = json.loads(content)

for question in data:
    print(question["question_text"].capitalize())
    for index,option in enumerate(question["alternatives"]):
        print(f"{index}-{option.capitalize()}")
    user_input = int(input("Enter your answer: "))
    if user_input == question["answer"]:
        correct_answer += 1
        
        
    else:
        incorrect_answer += 1
        
        
        



    
        