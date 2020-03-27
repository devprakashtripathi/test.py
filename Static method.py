# it is not work for the class variable or instance variable
# so if  want to do extar work it can be used

# her i want to print ablout the info not about the class or the student
# avg marks
class Student:
    school = 'ims'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def _getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is Student claas --------abc mobile")


s1 = Student(32, 45, 25)
s2 = Student(89, 55, 65)

print(s1.avg)
print(Student._getschool())
Student.info()
