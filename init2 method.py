# here work with behaviour.
# it is like constructor
# so it is autometicly called

class Computer:
    def _init_(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is", self.cpu, self.ram)


com1 = Computer('i5', 16)
com2 = Computer('ryzen', 8)

com1.config()
com2.config()
