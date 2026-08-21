from tkinter import *
window=Tk()
window.title("Event Handler")
window.geometry("100x100")
def handler_keypress(event):
    print(event.char)
window.bind("<Key>",handler_keypress)
def handle_click(event):
    print("the button was clicked")
button=Button(text="click me")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()