import statistics as st  # для подсчета средней оценки

a = 12
class Person:

    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduse_myself(self):
        print(f'Имя: {self.fullname}, Возраст: {self.age}, '
              f'Состоит в браке: {self.is_married}')


class Student(Person):

    def __init__(self, fullname, age, is_married, **marks):
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks

    # Подсчет средней оценки
    def calc_average_mark(self):
        if len(self.marks) != 0:
            return st.mean(self.marks.values())
        else:
            return "Оценок ещё нет"

    def print_marks(self):
        print("Оценки студента:")
        if len(self.marks) != 0:
            for i in self.marks:
                print(f'{i}: {self.marks[i]}')
            print(f'Средняя оценка: {self.calc_average_mark():.2f}')
        else:
            print("Оценок ещё нет")

    def introduse_myself(self):
        Person.introduse_myself(self)
        self.print_marks()


class Teacher(Person):
    salary = 25000.0

    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience

    def calc_salary(self):
        if int(self.experience) > 3:
            self.salary += (int(self.experience) - 3) * (self.salary / 100 * 5)

    def introduse_myself(self):
        Person.introduse_myself(self)
        print(f'Зарплата: {self.salary}')


def create_students():
    result = [Student("Ivan", 35, True, language=5, math=3, history=4),
              Student("Victor", 18, False, language=2, math=5, history=3),
              Student("Nikolai", 23, True, language=4, math=2, history=5)]
    return result


print("Учитель:")
teacher = Teacher("Victor Alekseevitch", 30, False, 4)
teacher.calc_salary()
teacher.introduse_myself()

print("Ученики:")
for i in create_students():
    print("------------------------------------------")
    i.introduse_myself()
