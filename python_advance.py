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

# s = "ABCD EF"
# s1 = "H" + s[1:]                  
# s2 = s.replace("ABC", "abc")  
# print(s)
# print(s1)
# print(s2)

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))
# s = "My name is {} and I am {} years old.".format( name, age)
# print(s)

# 1. Create a list of 5 students
# 2. Store name + marks using dictionaries
# 3. Print all students
# 4. Find highest marks
# 5. Find lowest marks
# 6. Calculate average


# students = [                                       # -- Creation of list of 5-6 students
#     {"Name" : "Aditya" , "Marks" : 90 },
#     {"Name" : "Kapil" , "Marks" : 75 },
#     {"Name" : "Yash" , "Marks" : 80 },
#     {"Name" : "Anuj" , "Marks" : 65 },
#     {"Name" : "Atharva" , "Marks" : 70 },
#     {"Name" : "Pranav" , "Marks" : 90 }
# ]                                                     # -- Store name + marks using dictionaries


# for s in students :                                    # -- Print all students name and marks
#     print(f"Name : {s["Name"]}  |  Marks : {s["Marks"]}")
# print(" ")

# highest = max(s["Marks"] for s in students)           # -- Find highest marks
# print(f"Highest Marks : {highest} \n")

# lowest = min(s["Marks"] for s in students)            # -- Find lowest marks
# print(f"Lowest Marks : {lowest} \n")

# marks = []
# for s in students:
#     marks.append(s["Marks"])

# total = sum(marks)
# print(f"Sum = {total}\n")

# avg = total/(len(marks))                          # -- Calculate average
# print(f"Average : {avg}")

names = ["Aditya", "Kapil", "Yash"]
marks = [85, 72, 91]
combined = list(zip(names, marks))
print(combined)  

for index, name in enumerate(names):
    print(f"Rank : {index+1} |", name)