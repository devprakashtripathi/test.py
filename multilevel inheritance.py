class A:
    def feature1(self):
        print("feature1 work")

    def feature2(self):
        print("feature2 is working")


class B(A):
    def feature3(self):
        print("feature 3 woriking")

    def feature4(self):
        print("feture 4 working")


class C(B):
    def featuire5(self):
        print("Feature 5 working")


a1 = A()
b1 = B()
c1 = C()
c1.feature1()  # so  here i can access all the feature of all the class
