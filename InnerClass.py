class Student:

    def __init__(self, Name, age):
        self.Name = Name
        self.age = age
        self.Lap = self.Laptop('2GB', 'AMD')

    def show(self):
        print(self.Name, self.age)
        self.Lap.show()

    class Laptop:

        def __init__(self, RAM, CPU):
            self.RAM = RAM
            self.CPU = CPU

        def show(self):
            print(self.RAM, self.CPU)


c1 = Student('Balraj', 25)
c2 = Student('Chandu', 33)
c1.show()
c2.show()
#Student.Laptop.show() --> This will not work