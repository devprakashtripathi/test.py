class A:
    def feature1(self):
        print("feature1 work")

    def feature2(self):
        print("feature2 is working")


class B():
    def feature3(self):
        print("feature 3 woriking")

    def feature4(self):
        print("feture 4 working")


class C(A, B):  # it is child class it ncan access all the feature of class A ,B
    def featuire5(self):
        print("Feature 5 working")


a1 = A()
a1.feature1()
b1 = B()
b1.feature3()
c1 = C()
c1.feature3()
c1.feature1()
c1.feature4()  # so  here i can access all the feature of all the class
