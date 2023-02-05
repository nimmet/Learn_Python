import json


correct_answer=0
incorrect_answer=0
answer = {}
q = 1

with open("quiz.json","r") as file:
    content = file.read()
    
data = json.loads(content)

for question in data:
    print(question["question_text"].capitalize())
    for index,option in enumerate(question["alternatives"]):
        print(f"{index}-{option.capitalize()}")
    user_input = int(input("Enter your answer: "))
    an={}
    an["user"] = user_input
    an["correct"] = question["answer"]
    answer[f"Q{q}"] = an 
    q += 1
        
for k,v in answer.items():
   
    if v["user"] == v["correct"]:
        user = v["user"]
        cor = v["correct"]
        print(f" {k} Correct Answer: User Answer: {user}, Correct Answer: {cor}")  
        correct_answer += 1
    else:
        user = v["user"]
        cor = v["correct"]
        print(f" {k} Incorrect Answer: User Answer: {user}, Correct Answer: {cor}")  
        incorrect_answer += 1
        
print(f"Score {correct_answer}/{correct_answer+incorrect_answer}")   

        
        
    
    
        