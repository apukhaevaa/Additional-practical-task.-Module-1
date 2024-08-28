# Пухаева Алина Александровна
#  Additional practical task.
# 28.08.2024
# Notes: ctrl+alt+L

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
print(students_sorted)
gpa = {student: sum(grades[t]) / len(grades[t]) for t, student in enumerate(students_sorted)}
print(gpa)
