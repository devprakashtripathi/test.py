class A:
    def __init__(self):
        print(" in A init")

    def feture1(self):
        print(" feature 1 is working")


class B(A):
    def __init__(self):
        super().__init__()
        print(" in B init")

    def feture1(self):
        print(" feature 1 is working")

    def feature2(self):
        print("feture 2 is working")


a1 = B()
