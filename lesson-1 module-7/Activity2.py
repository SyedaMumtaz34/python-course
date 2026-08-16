from tkinter import * 
from datetime import date
root=Tk()
root.title("getting started with widgets")
root.geometry("400x300")
label=Label(text="hey there!",fg="white",bg="#072F5F",height=1,width=300)
name_label=Label(text="full name",bg="#3895D3")
name_entry=Entry()
def display():
    name=name_entry.get()
    global Message
    Message="wellcome to the application! \nToday's date is:"
    greet="Hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,Message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
button=Button(text="begin",command=display,height=1,bg="#1261a0",fg="white")
label.pack()
name_label.pack()
name_entry.pack()
button.pack()
text_box.pack()
root.mainloop()
