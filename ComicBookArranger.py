#! /usr/bin/python
#
# CBA_Main_Window.py
#
# author : Ed Goodwin
# date : 05.25.2023
#

import os
import sys
import tkinter as tk

class CBA_Main_Window:
    
    window = tk.Tk()
    label = tk.Label(text = "CBArranger")
    menubar = tk.Menu(window)

    def __init__(self):
        return None
    
    def defineMenu(self):
        menubar = tk.Menu(CBA_Main_Window.window)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

    def run(self):
        CBA_Main_Window.defineMenu(self)
        CBA_Main_Window.label.pack()
        CBA_Main_Window.window.mainloop()

if __name__ == "__main__":
    cv = CBA_Main_Window()
    cv.run()