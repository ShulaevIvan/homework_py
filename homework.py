class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = 0

    def rate_lec(self, lec, course, grade):
        if isinstance(lec, Lecturer) and course in lec.courses_attached and course in self.courses_in_progress:
            if course in lec.grades and grade <= 10:
                lec.grades[course] += [grade]
            elif grade <= 10:
                lec.grades[course] = [grade]
        else:
            return 'Ошибка'

        sum = 0
        length = 0
        for k in lec.grades.values():
            for i in k:
               sum = sum + i
               length += 1
        lec.average = round(sum / length)

    def __lt__(self, obj):
        if not isinstance(obj, Student):
            print('ошибка')
            return
        return self.average < obj.average

    def __str__(self):
        out = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}'
        return out


        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades and grade <= 10:
                student.grades[course] += [grade]
            elif grade <= 10:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        sum = 0
        length = 0
        for k in student.grades.values():
            for i in k:
                length += 1
                sum = sum + i
        student.average = round(sum / length)

    def __str__(self):
        out = f'Имя: {self.name}\nФамилия: {self.surname}'
        return out

class Lecturer(Mentor):
    grades = {}
    average = 0

    def __lt__(self, obj):
        if not isinstance(obj, Lecturer):
            print('Ошибка')
            return
        return self.average < obj.average

    def __str__(self):
        out = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.average}'
        return out
    


 
best_student = Student('Ruoy', 'Eman', 'your_gender')
student_one = Student('Илья', 'Родионов', 'мж')
student_two = Student('Максим', 'Журавлёв', 'мж')

lecturer = Lecturer('Ruoy', 'Eman')
lecturer_one = Lecturer('Михаил', 'Фокин')
lecturer_two = Lecturer('Иван', 'Громов')

reviewer = Reviewer('Some', 'Buddy')

best_student.courses_in_progress += ['Python', 'Git']
student_one.courses_in_progress += ['Python', 'Git']
student_two.courses_in_progress += ['Python', 'Git']

best_student.finished_courses += ['Введение в программирование']
student_one.finished_courses += ['Введение в программирование']
student_two.finished_courses += ['Введение в программирование']

lecturer.courses_attached += ['Python']
reviewer.courses_attached += ['Python']
 
reviewer.rate_hw(student_one, 'Python', 5)
reviewer.rate_hw(student_two, 'Python', 6)
reviewer.rate_hw(best_student, 'Python', 7)

student_one.rate_lec(lecturer, 'Python', 8)
student_two .rate_lec(lecturer, 'Python', 9)
best_student.rate_lec(lecturer, 'Python', 10)
 
students_arr = [best_student, student_one, student_two]
lecturer_arr = [lecturer, lecturer_one, lecturer_two]

def average_all(arr, courses):
    sum_grade = 0
    i = 0
    for j in arr:
        for k, value in j.grades.items():
            if courses in k:
                sum_grade += sum(value) / len(value)
                i += 1
    return round(sum_grade / i)

print(lecturer)
print(student_one)
print(reviewer)

print(f'Средняя оценка студентов по Python: {average_all(students_arr, "Python")}')
print(f'Средняя оценка лекторов по Python: {average_all(lecturer_arr, "Python")}')







