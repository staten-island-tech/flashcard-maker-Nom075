import json

class Flashcard:
    def __init__ (self, question, answer):
        self.question = question
        self.answer = answer
    def display(self):
        return (f"{self.question} The answer is {self.answer}")



""" ans = input("Are you a teacher or Student? (Input T or S)")
if ans.upper() == "T":
    Pword = input("Enter valid teacher password")
    if Pword == "AAA":
        print("Valid passcode")
        Role = "T"
    else:
        print("Ur 100% a student.")
        Role = "S"
elif ans.upper() == "S":
    Role = "S"
else:
    print("Could not detect answer. Program shutting down...") """


flash = [
    Flashcard("Is Aaron dumb?", "Nah"),
    Flashcard("What is the sin of 30?", "1/2"),
    Flashcard("Darwin is dumb?", "Yes, he is.")

]

flash_data = [cards.__dict__ for cards in flash]

try:
    with open("flash.json", "r") as file:
        flash_data = json.load(file)
except FileNotFoundError:
    flash_data = []

for card in flash:
    print(card.display())

with open("flash.json", "w") as file:
    json.dump(flash_data, file, indent=4)

