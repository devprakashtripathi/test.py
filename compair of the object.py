class computer:
    def __init__(self):
        self.name = "Dev"
        self.age = 23

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = computer()

c1.name = "sweta"
c1.age = 28
c2 = computer()
if c1.compare(c2):
    print("they are same ")
else:
    print("They are not same")

print(c1.name)
print(c2.name)
