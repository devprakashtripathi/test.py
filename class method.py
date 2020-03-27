# example for the class variable
# so for instance varr we use (self) keyword and for class we use the (cls) keyword


class Student:
    school = "ims"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod  # decorator @(sign) for use the decorator of the class
    def info(cls):  # cls is the class variable for all object
        return cls.school


s1 = Student(34, 35, 38)
s2 = Student(25, 34, 57)

print(s1.avg())
print(Student.info())
