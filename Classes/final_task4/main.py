class Student:
    def __init__(self, name, surname, gender):
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__finished_courses = []
        self.__courses_in_progress = []
        self.__grades = {}

    def add_courses(self, course_name):
        self.__finished_courses.append(course_name)

    def get_finished_courses(self):
        return self.__finished_courses

    def set_courses_in_progress(self, courses):
        self.__courses_in_progress += courses

    def get_courses_in_progress(self):
        return self.__courses_in_progress

    def set_courses_grade(self, course, grade):
        if course in self.__grades:
            self.__grades[course] += [grade]
        else:
            self.__grades[course] = [grade]

    def get_grade(self):
        return self.__grades

    def get_avg_grade(self) -> float:
        marks = 0
        count = 0
        for list_grades in self.__grades.values():
            marks += sum(list_grades)
            count += len(list_grades)

        if count != 0:
            avg_marks = marks / count
            return avg_marks
        else:
            return 0

    def __eq__(self, other):
        return self.get_avg_grade() == other.get_avg_grade()

    def __str__(self):
        return (f"Имя: {self.__name} \n"
                f"Фамилия: {self.__surname} \n"
                f"Средняя оценка за домашние задания: {self.get_avg_grade()} \n"
                f"Курсы в процессе изучения: {','.join(self.__courses_in_progress)} \n"
                f"Завершенные курсы: {','.join(self.__finished_courses)} \n")


    def take_rate_for_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.get_courses_attached() and course in self.__courses_in_progress:
            lecturer.set_courses_grade(course, grade)
        else:
            return 'Ошибка'



class Mentor:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.__courses_attached = []

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def set_courses_attached(self, course):
        self.__courses_attached += course

    def get_courses_attached(self):
        return self.__courses_attached


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.__courses_grade = {}

    def set_courses_grade(self, course, grade):
        if course in self.__courses_grade:
            self.__courses_grade[course] += [grade]
        else:
            self.__courses_grade[course] = [grade]

    def get_courses_grade(self):
        return self.__courses_grade

    def get_avg_grade(self) -> float:
        marks = 0
        count = 0
        for list_grades in self.__courses_grade.values():
            marks += sum(list_grades)
            count += len(list_grades)
        if count != 0:
            avg_marks = marks / count
            return avg_marks
        else:
            return 0

    def __eq__(self, other):
        return self.get_avg_grade() == other.get_avg_grade()

    def __str__(self):
        return (f"Имя: {self.get_name()} \n"
                f"Фамилия: {self.get_surname()} \n"
                f"Средняя оценка за лекции: {self.get_avg_grade()} \n")


class Reviewer(Mentor):
# ну увидела смысла в init, т.к. в этом классе нет новых переменных
    def __str__(self):
        return (f"Имя: {self.get_name()} \n"
                f"Фамилия: {self.get_surname()} \n")

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.get_courses_attached() and
                course in student.get_courses_in_progress()):
            student.set_courses_grade(course, grade)
        else:
            return 'Ошибка'

def get_avg_grade_all_students(students_list: list, choose_course: str):
    marks = 0
    count = 0
    for student in students_list:
        if isinstance(student, Student) and choose_course in student.get_courses_in_progress():
            marks += sum(student.get_grade()[choose_course])
            count += len(student.get_grade()[choose_course])
        else:
            print(f"{student} не студент или {choose_course} этот студент не изучает")
            return 0

    if count != 0:
        avg_marks = marks / count
        return avg_marks
    else:
        return 0

def get_avg_grade_all_lecturers(lecturers_list: list, select_course: str):
    marks = 0
    count = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and select_course in lecturer.get_courses_attached():
            marks += sum(lecturer.get_courses_grade()[select_course])
            count += len(lecturer.get_courses_grade()[select_course])
        else:
            print(f"{lecturer} не лектор или {select_course} этот лектор не ведет")
            return 0
    if count != 0:
        avg_marks = marks / count
        return avg_marks
    else:
        return 0


if __name__ == '__main__':
    Alenka = Student("Alena", "Ponomareva", "female")
    Alenka.set_courses_in_progress(["Python","C++"])

    Aleksander_Budanyan = Student("Aleksander", "Budanyan", "male")
    Aleksander_Budanyan.set_courses_in_progress(["Java", "C++"])

    Aleksander = Reviewer("Aleksander", "Bardin")
    Aleksander.set_courses_attached(["Python","C++"])
    Aleksander.rate_hw(Alenka, "Python", 10)
    Aleksander.rate_hw(Alenka, "Python", 9)
    Aleksander.rate_hw(Alenka, "C++", 8)
    Aleksander.rate_hw(Alenka, "C++", 10)
    Aleksander.rate_hw(Aleksander_Budanyan, "C++", 7)

    Olga = Reviewer("Olga", "Buzova")
    Olga.set_courses_attached(["Java"])
    Olga.rate_hw(Aleksander_Budanyan, "Java", 10)
    Olga.rate_hw(Aleksander_Budanyan, "Java", 8)


    Sonya = Lecturer("Sonya", "Poltavskaya")
    Sonya.set_courses_attached(["Python","C++"])
    Oleg = Lecturer("Oleg", "NormName")
    Oleg.set_courses_attached(["Java", "Python"])

    Aleksander_Budanyan.take_rate_for_lector(Oleg, "Java", 10)
    Aleksander_Budanyan.take_rate_for_lector(Oleg, "Java", 6)
    Alenka.take_rate_for_lector(Sonya, "Python", 8)
    Alenka.take_rate_for_lector(Sonya, "C++", 10)
    Alenka.take_rate_for_lector(Sonya, "C", 10) # проверка вычисления средней оценки с отсутствующим предметом
    Alenka.take_rate_for_lector(Oleg, "Python", 10)
    
    Alenka.add_courses("JavaScript")
    Aleksander_Budanyan.add_courses("JavaScript")

    print(Alenka)
    print(Aleksander_Budanyan)
    print(Aleksander)
    print(Olga)
    print(Sonya)
    print(Oleg)

    print(f"Равны ли средние оценки лектора Олега и студента Александра? "
          f"{Aleksander_Budanyan.__eq__(Oleg)}")

    students = [Alenka, Aleksander_Budanyan]
    print(get_avg_grade_all_students(students, "C++"))

    lecturers = [Sonya, Oleg]
    print(get_avg_grade_all_lecturers(lecturers, "Python"))



