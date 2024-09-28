class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def get_avg_grade(self) -> float:
        marks = 0
        count = 0
        for list_grades in self.grades.values():  # TODO: вынести в отдельную функцию
            marks += sum(list_grades)
            count += len(list_grades)

        avg_marks = marks / count
        return avg_marks

    def __eq__(self, other):
        return self.get_avg_grade() == other.get_avg_grade()

    def __str__(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Средняя оценка за домашние задания: {self.get_avg_grade()}")
        print(f"Курсы в процессе изучения: {','.join(self.courses_in_progress)}")
        print(f"{','.join(self.finished_courses)}")

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def take_rate_for_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses and course in self.courses_in_progress:
            if course in lecturer.courses_grade:
                lecturer.courses_grade[course] += [grade]
            else:
                lecturer.courses_grade[course] = [grade]
        else:
            return 'Ошибка'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self):
        super().__init__()
        self.courses_grade = {}
        self.courses = []

    def get_avg_grade(self) -> float:
        marks = 0
        count = 0
        for list_grades in self.courses_grade.values():
            marks += sum(list_grades)
            count += len(list_grades)

        avg_marks = marks / count
        return avg_marks

    def __eq__(self, other):
        return self.get_avg_grade() == other.get_avg_grade()

    def __str__(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Средняя оценка за лекции: {self.get_avg_grade()}")


class Reviewer(Mentor):

    def __str__(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

