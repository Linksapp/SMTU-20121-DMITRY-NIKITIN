class Learner:
    def __init__(self):
        self.classes = []
    def enroll(self, course):
        self.classes.append(course)
class Teacher:
    def __init__(self):
        self.courses_taught = []
    def assign_teaching(self, course):
        self.courses_taught.append(course)

class Person:
    def __init__(self, name, surname, number, learner: Learner=None, teacher: Teacher=None):
        self.name = name
        self.surname = surname
        self.number = number

        self.learner = learner
        self.teacher = teacher
    def enroll(self, course):
        try:
            self.learner.enroll(course)
        except:
            print('Параметр learner не передан')
    def assign_teaching(self, course):
        try:
            self.teacher.assign_teaching(course)
        except:
            print('Параметр teacher не передан')

jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())
jane.enroll('a_postgrad_course')
jane.assign_teaching('an_undergrad_course')
