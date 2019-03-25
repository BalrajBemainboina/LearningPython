class Computer:
    Wheels = 4

    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu

    def config(self):
        print("Configuration of the computer", self.cpu, self.ram)

    def compare(self,other):
        if self.ram ==  other.ram:
            return True
        else:
            return False

    @staticmethod
    def info():
        print ('Executing from the Static Method')

    @classmethod
    def getWheels(cls):
        return cls.Wheels


com1 = Computer('3gb', 'i5')
com2 = Computer('3gb', 'AMD')
com1.config()
com2.config()
print (Computer.getWheels())
Computer.info()
print(Computer.Wheels)
print(com1.Wheels)
Computer.Wheels = 5
print(com2.Wheels)
val = com1.compare(com2)
if val==True:
    print("RAM same")

