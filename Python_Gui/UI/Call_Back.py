from tkinter import *
from tkinter import ttk


def BUclick(id):
    print("id:{}".format(id))

root = Tk()

button = ttk.Button(root,text="click me " , command=lambda :BUclick(id=10)).pack()

root.mainloop()