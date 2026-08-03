from abc import ABC,abstractmethod
class Animal(ABC):
    def move (self):
        pass
class Human(Animal):
    def move (self):
        print("I can walk and run: ")
class Snake(Animal):
    def move (self):
        print("I can crawl")
class dog (Animal):
    def move (self):
        print("i can bark ")
class lion(Animal):
    def move (self):
        print("I can roar ")
r=Human()
r.move()
k=Snake()
k.move()
d=dog()
d.move()
l=lion()
l.move()