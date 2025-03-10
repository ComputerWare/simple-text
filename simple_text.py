#simple_text.py
#Simple text module by ComuterWare

from tkinter import Label
class ST(Label):
    def __init__(self, t, w):
        Label(w, text=t).pack()

#usage is very simple:
#just call the function with:
#ST(w=parent-tk-process, t="text goes here!!")
