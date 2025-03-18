courses = { 
    "Python Programming": {"fee": 150, "seats": 0, "category" : "Technology"},
    "Machine Learning": {"fee": 200, "seats": 3, "category" : "Technology"},
    "Business Strategy": {"fee": 100, "seats": 5, "category" : "Business"},
    "Marketing 101": {"fee": 120, "seats": 2, "category" : "Business"},
    "Cybersecurity": {"fee": 100, "seats": 4, "category" : "Technology"},


}

student_enrollment = ["Python Programming", "Business Strategy", "Marketing 101"]
final_enroll = []

""" 
for count, course in enumerate(student_enrollment, start = 1):
    if count >= 3:
        print("Applying discount") """

for count, course in enumerate(student_enrollment, start = 1):
    if courses[course]["seats"] == 0:
        full = courses[course]
        for selection in courses:
            if courses[selection]["category"] == "Technology" and courses[selection]["seats"] > 0:
                print(f"{full} is full. Suggested course: {selection}")
                break
    else:
        final_enroll.append(course)
        
    if count >= 3:
        print("Applying 5% discount")

    if courses[course]["category"] == "Technology":
        print("$20 discount")
