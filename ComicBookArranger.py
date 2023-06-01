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

    def __init__(self):
        return None
    
    def run(self):
        CBA_Main_Window.label.pack()
        CBA_Main_Window.window.mainloop()

if __name__ == "__main__":
    cv = CBA_Main_Window()
    cv.run()