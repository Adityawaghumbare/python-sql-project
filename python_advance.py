# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = []
# for n in numbers:
#     squares.append(n**2)

# print(squares)

# student = { "Name" : "Aditya" , "Marks": 85, "Attendance": 90 }
# print(student)
# print(student["Name"])
# print(student.keys())
# print(student.values())

# students = [
#     {"name": "Aditya", "marks": 85, "attendance": 90},
#     {"name": "Rohan", "marks": 72, "attendance": 65},
#     {"name": "Priya", "marks": 91, "attendance": 95},
# ]

# for n in students:
#     print(n["name"], n["marks"])

# total_marks = sum(s["marks"] for s in students)
# average_marks = total_marks / len(students)
# print(" Total Marks : ", total_marks,"/", len(students*100), "\n","Average Marks : ",  average_marks)

s = "ABCD EF"
s1 = "H" + s[1:]                  
s2 = s.replace("ABC", "abc")  
print(s)
print(s1)
print(s2)