import json

class Flashcard:
    def __init__ (self, question, answer):
        self.question = question
        self.answer = answer
    def display(self):
        return (f"{self.question}? The answer is {self.answer}")



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



Flashcards = [Flashcard(input("Enter a valid question"), input("Enter an answer"))]
print(Flashcards)