
from tkinter import *

from tkinter import *
root = Tk()
opt=['Jan', 'Feb', 'March']

var = StringVar(root)  # initialization of a common StringVar for both OptionMenu and Label widgets

class MyOptMenu(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        var.set(opt[0])  # give an initial value to the StringVar that will be displayed first on the OptionMenu
        self.om = OptionMenu(self, var, *opt)
        self.om.pack(side=TOP)
        var.trace('w', self.getValue)   # continuously trace the value of the selected items in the OptionMenu and update the var variable, using the function self.getValue
    def getValue(self, *args):
        return(var.get())  # return the current value of OptionMenu

class MyLabel(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()
        self.lab = Label(self, textvariable = var, bg='white')  # use the same StringVar variable (var) as the OptionMenu. This allows changing the Label text instantaneously to the selected value of OptionMenu
        self.lab.pack(side=TOP)

a = MyOptMenu(root)
b = MyLabel(root)
root.mainloop()

