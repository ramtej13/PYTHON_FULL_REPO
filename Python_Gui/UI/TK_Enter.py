
from tkinter import*
from tkinter import ttk


root = Tk()
entry = ttk.Entry(root,width=30)
entry.pack()
button=ttk.Button(root,text="click me!")
button.pack()
button=ttk.Button(root,text="click me!")
button.pack()
button=ttk.Button(root,text="click me!")
button.pack()

def BuClick():
    print(entry.get())
    entry.delete(0,3)
    # entry.insert(0,"button clicked")

button.config(command=BuClick())



root.mainloop()





