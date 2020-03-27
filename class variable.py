class car:
    wheel = 4  # it is the class variable belong to the classnamesapce

    def __init__(self):
        self.mailage = 10  # so it is the instance variable because it is  define in the init method not in the class
        self.company = 'BMW'  # instance variable belongs to instance namespace


c1 = car()  # calling the object
c2 = car()
car.wheel = 5  # here we call the class variable for
c1.mailage = 8
print(c1.company, c1.wheel)
print(c2.company, c2.wheel)
