from abc import ABC,abstractmethod
class Abs(ABC):
    def print(self,x):
        print("passed value ",x)
    @abstractmethod
    def task(self):
        print("we are inside abstract class task: ")
class testclass(Abs):
    def task (self):
        print("we are inside test class task: ")
test_object=testclass()
test_object.task()
test_object.print (100)