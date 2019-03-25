class A:

    def __init__(self):
        print ("init of Class A")

    def feature1(self):
        print("Feature1 is working")

    def feature2(self):
        print("Feature2 is Working")


class B():

    def __init__(self):
        print ("init of Class B")

    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is Working")


class C(A, B):

    def __init__(self):
        print ("init of Class C")
        super().__init__()

    def feature5(self):
        print("Feature4 is working")
        super().feature1()

    def feature6(self):
        print("Feature5 is Working")
feat=C()
feat.feature1()
feat.feature2()
feat.feature3()
feat.feature4()
feat.feature5()