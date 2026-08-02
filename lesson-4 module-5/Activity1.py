class MyClass:
    __privateVar=27;
    def __privatemethod(self):
        print("i'm inside Myclass")
    def Hello(self):
        print("Private variable value ",MyClass.__privateVar)
a=MyClass()
a.Hello()
a.__privatemethod


