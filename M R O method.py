class A:
    def __init__(self):
        print(" in A init")

    def feture1(self):
        print(" feature 1 a is working")


class B(A):
    def __init__(self):
        super().__init__()
        print(" in B init")

    def feture1(self):
        print(" feature 1 b is working")
GGG
    def feature2(self):
        print("feture 2 is working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("in c init")

    def feat(self):
        super().feature2()


a1 = C()
a1.feat()
