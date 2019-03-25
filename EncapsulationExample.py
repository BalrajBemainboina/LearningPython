class Car:

    def __init__(self,color,speed):
        self.__color = color
        self.__speed = speed
        self.__Displayinfo()

    def get_speed(self):
        return self.__speed

    def set_speed(self,speed):
        self.__speed = speed

    def set_color(self,color):
        self.__color = color

    def get_color(self):
        return self.__color

    def __Displayinfo(self):
        print("This is the information of car : color {} speed {}".format(self.__color,self.__speed))


Honda = Car('Red', 200)
Ford = Car('White', 300)
print(Honda.get_color())
print(Honda.get_speed())
print(Ford.get_color())
print(Ford.get_speed())
Honda.__color = 'black'  # Though you are changing color of honda it is still not changed as it is private hence you cannot change, you can change with set
print(Honda.get_color())
Honda.set_color('black')
print(Honda.get_color())
#Honda.__Displayinfo() --> Not accepted as private methods cannot be called
#Ford.__Displayinfo() --> Not accepted as private method cannot be called.