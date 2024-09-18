# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:43:50 2024

@author: liang
"""

import tkinter as tk
window = tk.Tk()
window.title("我的第一個GUI程式")
window.geometry('300x300')
label = tk.Label(window, text = "HEllO!")
label.pack()
entry = tk.Entry(window, width = 20)
entry.pack()
button = tk.Button(window, text = "我是按鈕")
window.mainloop()