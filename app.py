import json

class Flashcard:
    def __init__ (self, question, answer):
        self.question = question
        self.answer = answer
    def display(self):
        return (f"{self.question} The answer is {self.answer}")



ans = input("Are you a teacher or Student? (Input T or S)")
if ans.upper() == "T":
        Role = "T"
elif ans.upper() == "S":
    Role = "S"
else:
    print("Could not detect answer. Program shutting down...")


flash = [
    Flashcard("Is Aaron dumb?", "Nah"),
    Flashcard("What is the sin of 30?", "1/2"),
    Flashcard("Darwin is dumb?", "Yes, he is.")

]

flash_data = [cards.__dict__ for cards in flash]

def Card_Loader(flash_data):
    try:
        with open("flash.json", "r") as file:
            flash_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        flash_data = []

    if not flash_data:
        flash_data = [cards.__dict__ for cards in flash]


    with open("flash.json", "w") as file:
        json.dump(flash_data, file, indent=4)

    for card in flash:
        print(card.display())

    return flash_data

flash_data = Card_Loader([])




Card_Loader(flash_data)