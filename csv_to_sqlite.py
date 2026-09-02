import csv

students = []

with open('students.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
      row["marks"] = int(row["marks"])
      row["attendance"] = int(row["attendance"])
      students.append(row)
      print(row)

print(students[0]["marks"] + 15)

for s in students:
    if s["marks"] > 100 or s["marks"] < 0 :
        print(f"Invalid marks for {s["name"]}")