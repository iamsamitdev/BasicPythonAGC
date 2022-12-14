import tkinter as tk
from tkinter import ttk
from subprocess import Popen
import clipboard

mainfrm = tk.Tk()
mainfrm.geometry("300x200")


def open_calc():
    Popen("calc.exe")


def open_notepad():
    Popen("notepad.exe")


# C:\Program Files (x86)\Seagull\BarTender UltraLite
def onpen_bartender():
    Popen(['C:\Program Files (x86)\Seagull\BarTender UltraLite\BarTend.exe'])


def copyClipboard():
    clipboard.copy("abc")  # now the clipboard content will be string "abc"
    text = clipboard.paste()  # text will have the content of clipboard
    print(text)


btn = ttk.Button(mainfrm, text="Open Calculator", command=open_calc, width=100)
btn.pack(padx=20, pady=5)

btn = ttk.Button(mainfrm, text="Open Notepad", command=open_notepad, width=100)
btn.pack(padx=20, pady=5)

btn = ttk.Button(mainfrm, text="Open BarTender",
                 command=onpen_bartender, width=100)
btn.pack(padx=20, pady=5)

btn = ttk.Button(mainfrm, text="Paste Clipboard",
                 command=copyClipboard, width=100)
btn.pack(padx=20, pady=5)

mainfrm.mainloop()
