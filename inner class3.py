class student:  # this is outer class
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()  # here i declare the variable

    def show(self):  # show method of student class
        print(self.name, self.rollno)

    class Laptop:  # this is the inner class  of student
        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.rum = 8


s1 = student('dev', 2)
s2 = student('ved', 3)

s1.show()
lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))  # it means both print of lap1 and lap2  take different memory address
print((id(lap2)))
