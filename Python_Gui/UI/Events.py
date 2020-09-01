from tkinter import *
from tkinter import ttk

root =Tk()


def key_press(event):
    print("typ:{}".format(event.type))


def Button_press(event):
    print("button press")


Bu = ttk.Button(root,text="click me")
Bu.pack()
Bu.bind("<ButtonPress>",Button_press)
root.bind("<Control-c>",key_press)





root.mainloop()