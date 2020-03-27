# class will have variable and method/function
class Student:
    def _init_(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name, self.rollno)


s1 = Student('Dev', 2)
s1.show()
