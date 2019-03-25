from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def move(self):
        pass


class Human(Animal):

    def move(self):
        print('Human can walk and Run')


class Snake(Animal):

    def move(self):
        print("Snake can crawl")


s = Snake()
h = Human()
s.move()
h.move()
# a = Animal() --> THis will not work as Animal is a abstract class hence it cannot be instantiated
