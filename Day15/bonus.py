import json

with open("quiz.json","r") as file:
    content = file.read()
    
data = json.loads(content)

for question in data:
    print(question["question_text"])