# Данные входные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Сначала нужно отсортировать список оценок и сопоставить их с именами студентов в алфавитном порядке
sorted_students = sorted(students)
student_grades_dict = {}

# Заполняем словарь средними баллами
for i in range(len(sorted_students)):
    student_name = sorted_students[i]
    student_grades = grades[i]
    average_grade = sum(student_grades) / len(student_grades)
    student_grades_dict[student_name] = average_grade

# Вывод результата
for student, avg_grade in student_grades_dict.items():
    print(f'Средний балл у {student}: {avg_grade:.2f}')