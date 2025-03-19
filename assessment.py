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
        full = course
        for selection in courses:
            if courses[selection]["category"] == courses[full]["category"] and courses[selection]["seats"] > 0:
                print(f"{full} is full. Suggested course: {selection}")
                final_enroll.append(selection)
                break
    else:
        final_enroll.append(course)
        
    if count >= 3:
        print("Applying 5% discount for enrolling in more than 3 courses")
        Percent_discount = 0.05

    if courses[course]["category"] == "Technology":
        print("Applying $20 scholarship for enrolling in a Technology course")
        num_discount = 20


cost = 0
for course in final_enroll:
    cost += courses[course]["fee"]
print(f"Total enrollment cost before discounts: {cost}$")
cost = cost * (1-Percent_discount)
cost = cost - num_discount

print(f"Total enrollment cost after discounts: {cost}$")