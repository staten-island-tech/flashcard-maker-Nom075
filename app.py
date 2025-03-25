import json
import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display(self):
        return f"Question: {self.question}? The answer is {self.answer}"

# Ask for role
ans = input("Are you a teacher or Student? (Input T or S): ")
if ans.upper() == "T":
    Role = "T"
elif ans.upper() == "S":
    Role = "S"
else:
    print("Could not detect answer. Program shutting down...")
    exit()


try:
    with open("flash.json", "r") as file:
        flash_data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    flash_data = []


while True:
    if Role == "T":

        question = input("Enter a question: ")
        answer = input("Now enter the answer: ")
        flash_data.append({"question": question, "answer": answer})


        with open("flash.json", "w") as file:
            json.dump(flash_data, file, indent=4)


        for card in flash_data:
            print(f"{card['question']} The answer is {card['answer']}")

        command = input("Got more cards? Y/N: ").strip().upper()
  

        if command != "Y":
            break
    
    
    if Role == "S":
        try:
            with open("flash.json", "r") as file:
                flash_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            flash_data = []
        
        streak = 0
        Points = 0
        while True:
            question = random.choice(flash_data)
            if input(question["question"]).lower() == question["answer"].lower():
                Points += (1+(streak/5))
                print(f"Correct! You gained {(1+(streak/5))} points.")
                print(f"Current points: {Points}")
                streak += 1
                print(f"Current streak: {streak}")

            else: 
                streak = 0
                print(f"The correct answer was {question["answer"]}. Your streak has been reset to {streak}.")
                print(f"Current points: {Points}.")
            if input("Continue? Y/N").upper() != "Y":
                break


        break

print("Program shutting down...")