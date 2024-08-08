#simple_text.py
#Simple text module by ComuterWare

from tkinter import Label
class ST(Label):
    def __init__(self, tex, window):
        Label(window, text=tex).pack()

#usage is very simple:
#just call the function with:
#ST(window=parent-tk-process, tex="text goes here!!")
