import json


ans = input("Are you a teacher or Student? (Input T or S)")
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
    print("Could not detect answer. Program shutting down...")

