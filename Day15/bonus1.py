import json

with open("quiz.json","r") as file:
    content = file.read()
    
data = json.loads(content)

for question in data:
    print(question["question_text"])
    
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, "-", alternative)
    
    user_choice = int(input("Enter you answer: "))
    question["user_choice"] = user_choice
    
    
        

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["answer"]:
        score += 1
        result = "Correct answer"
    else:
        result = "Wrong answer"
        
    message = f"{index+1} {result} - Your answer: {question['user_choice']}, " \
        f"Correct answer: {question['answer']}"
    print(message)
    

print(f"Score {score} / {len(data)}") 

