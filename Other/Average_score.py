grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

count = 0
student_book = dict()
for student in students:
    ave_score = (sum(grades[count]) / len(grades[count]))
    student_book[student] = round(ave_score, 2)
    count += 1

print(student_book)


