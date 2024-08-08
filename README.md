# simple-text
This is a Python3 Tkinter based library for a simple text widget.<br>
The usage is simple:<br>
`ST(window=parent-window, tex="this is the text")`<br>
Just do not forget to import the main library :)
`from tkinter import Label
class ST(Label):
    def __init__(self, tex, window):
        Label(window, text=tex).pack()`
