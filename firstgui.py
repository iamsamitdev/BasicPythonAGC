# โหลดโมดูล tkinter เข้ามายังโปรแกรมทุกคลาส
import tkinter as tk
from tkinter import ttk
from subprocess import Popen
import clipboard

# สร้างออบเจ็ค mainfrm
mainFrm = tk.Tk()

# แสดงข้อความที่ title bar
mainFrm.title('โปรแกรม GUI ด้วยไพทอน')

# กำหนดความกว้าง สูง ระยะห่างแกน x ระยะห่างแกน y
mainFrm.geometry("300x200+10+20")


# สร้างฟังก์ชันสำหรับการเรียกใช้ที่ปุ่ม
def show_hello():
    print("Hello form gui")


def open_calc():
    Popen("calc.exe")


def open_bandicam():
    Popen([r'C:\Program Files (x86)\Bandicam\bdcam.exe'])


def onpen_bartender():
    clipboard.copy('447947947984')
    Popen(['C:\Program Files (x86)\Seagull\BarTender UltraLite\BarTend.exe'])


# เพิ่มปุ่ม button
btn = ttk.Button(mainFrm, text="Hello", width="20", command=show_hello)
btn.pack(padx=20, pady=5)

# เพิ่มปุ่ม button
btn = ttk.Button(mainFrm, text="Open Calculator",
                 width="20", command=open_calc)
btn.pack(padx=20, pady=5)

btn = ttk.Button(mainFrm, text="Open Bandicam",
                 width="20", command=open_bandicam)
btn.pack(padx=20, pady=5)

btn = ttk.Button(mainFrm, text="Open BarTender",
                 command=onpen_bartender, width=100)
btn.pack(padx=20, pady=5)

# คำสั่งแสดงผลหน้า GUI
mainFrm.mainloop()
