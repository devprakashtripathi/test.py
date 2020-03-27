class car:
    def __init__(self):
        self.mailage = 10  # so it is the instance variable because it is  define in the init method not in the class
        self.company = 'BMW'


c1 = car()  # calling the object
c2 = car()
c1.mailage = 8
print(c1.company, c1.mailage)
print(c2.company, c2.mailage)
