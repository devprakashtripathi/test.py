class A:  # it is parent class A or Supper class
    def feature1(self):
        print("feature1 working")

    def feature2(self):
        print("feature 2 is working")


class B(A):  # sub class B is Aa child class or subclass so it can access the feature of class A so it is inheriting
    def feature3(selfs):
        print("ferature 3 is working")

    def feature4(self):
        print("feature 4 is working")


a1 = A()
a1.feature1()
a1.feature2()

b1 = B()  # it can inhetating all the feature A and of class B
b1.feature2()
b1.feature3()
