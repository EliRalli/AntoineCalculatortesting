# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:32:22 2020

@author: bofoi
"""

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import *

dfData=pd.read_excel('C:/Users/bofoi/PythonScript/Antoine_Constants_1.xlsx',Sheet_Name= 'Sheet 1')

items = ['-']+sorted(dfData['Chemical'].unique().tolist())
root= tk.Tk()

# class MyOptionMenu(OptionMenu):
#     def __init__(self, master, status, *options):
#         self.var = StringVar(master)
#         self.var.set(status)
#         OptionMenu.__init__(self, master, self.var, *options)
#         self.config(font=('calibri',(20)),bg='white',width=20)
#         self['menu'].config(font=('calibri',(12)),bg='white')


# root2 = Tk()
# optionList = items
# mymenu1 = MyOptionMenu(root2, 'Choose a Chemcial', *optionList)

# mymenu1.pack()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()


label1 = tk.Label(root, text='Enter a Temperature')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type your Number:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot ():
    
    x1 = entry1.get()
    
    label3 = tk.Label(root, text= 'The Square Root of ' + x1 + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    
    label4 = tk.Label(root, text= float(x1)**0.5,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()