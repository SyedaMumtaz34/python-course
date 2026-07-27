#student Grade book

#dictinary to add student names and marks
students={}
def add_students():
    for i in range(5):
        name=input("enter a student name: ")
        marks=input("enter a student marks: ")
        students[name]=marks 
def display_students():
    print("\n Students records ")
    highest=80
    lowest=30

def top_scorer():
    highest=max(students.values)
    for name,marks:
        students.items()
        if marks == highest:
            print("top_scorer=",name)
def bottom_scorer():
    lowest=min(students.values)
    for name,marks 
    students.items()
    if marks==lowest
    print("bottom_scorer=",name)
def average_marks():
    total=sum(students.values)
    average=total/len(students)




