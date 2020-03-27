class computer:
    def __init__(self):
        self.name = "Dev"
        self.age = 23

    def update(
            self):  # this self directing to the c1(object) so it is important and here the self is like a pointer which point the object whic i want to update
        self.age = 30


c1 = computer()
c2 = computer()

c1.name = "sweta"
c1.age = 28

c1.update()  # calling the update function for the self
c2.update()
print(c1.name)
print(c2.name)
