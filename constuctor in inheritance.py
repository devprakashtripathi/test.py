class A:
    def __init__(self):
        print("in a init")

    def feature1(self):
        print("feature1 work")

    def feature2(self):
        print("feature2 is working")


class B(A):
    def feature1(self):
        print("feature 1 woriking")

    def feature4(self):
        print("feture 4 working")


a = B()  # it will call the constroctor of A.
