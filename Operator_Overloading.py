class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        self.m1 = self.m1 + other.m1
        self.m2 = self.m2 + other.m2
        S3 = Student(self.m1,self.m2)
        return S3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


S1 = Student(58, 69)
S2 = Student(33, 44)
S3 = S1+S2
'''---> Ideally you cannot add two student objects, But we have overloaded + operator by overiding __add__ method'''
if S1 > S2:
    print ("S1 Win")
else:
    print("S2 Win")
'''--->Again above we have seen we can compare two student objects , 
We have overidden greath than > operator to compare by overiding gt func'''
print (S3.m1,S3.m2)
