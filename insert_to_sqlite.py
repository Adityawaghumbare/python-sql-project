import csv
import sqlite3

students = []

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["marks"] = int(row["marks"])
        row["attendance"] = int(row["attendance"])
        students.append(row)

for s in students:
    if s["marks"] < 0 or s["marks"] > 100:
        print(f"Invalid marks for {s['name']}")

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        marks INTEGER,
        attendance INTEGER
    )
""")

conn.commit()

for s in students:
    cursor.execute(
        "INSERT INTO students (name, marks, attendance) VALUES (?, ?, ?)",
        (s["name"], s["marks"], s["attendance"])
    )

conn.commit()

cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

conn.close()