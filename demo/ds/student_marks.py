data = [(1, 40), (3, 90), (3, 80), (2, 55), (1, 70), (5, 88)]

students = {}

for rollno, marks in data:
    total = students.get(rollno, 0)
    students[rollno] = total + marks

print(students)
