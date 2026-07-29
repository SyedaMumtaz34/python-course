class Employee:
    def __init__(self):
        print("employee created ")
    def __del__(self):
        print("destructor called ")
def create_object():
    print("making object ")
    obj=Employee()
    print("function end ")
    return obj
print("calling create_object()function ")
obj=create_object()
print("program end ")