class Student():
    school = "ims"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1_(self):
        return self.m1  # the for access and fetch the value of the instance variable

    def __set__m1_(
            self):  # the set method is use to modificaton of the value and it set the value of insatance vairable
        self.m1 = "value"


s1 = Student(34, 47, 58)
s2 = Student(89, 56, 25)

print(s1.avg())
