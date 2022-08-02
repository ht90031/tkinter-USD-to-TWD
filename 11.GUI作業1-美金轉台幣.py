"""
======第一題======
美金轉換後的台幣金額：
"""
# MIT License: Jamie Chuang
# powenko
# You XUAN新增圖片、底色～～
import tkinter as tk                     # 在Python 3.x 匯入該tkinter 函式庫
from PIL import ImageTk, Image

win = tk.Tk()                            # 建立GUI 應用程式的主視窗
win.wm_title("美金轉台幣")                 # 設定主視窗標題
win.resizable(width=False, height=False) # 設定主視窗不可以被調整大小
win.minsize(width=360, height=240)       # 最小尺寸
win.maxsize(width=360, height=240)       # 最大尺寸
x = Image.open("#c1c0b9.png")                   # 讀取圖片（背景）
img = ImageTk.PhotoImage(x)                     # 轉換成PhotoImage
labelBackground = tk.Label(win, image=img)      # 建立Label物件 顯示圖片（背景）
labelBackground.pack()                          # 置入圖片（背景）


total = 0
def event1():
    global total
    # try except會略過錯誤，盡量不要太常做，可能會發現不了程式碼存在的錯誤
    try:                 # 嘗試處理
        total = float(entry1Str.get()) * 29.82
    except:              # 如果失敗
        total = 0
    # 另一種寫法，判斷是不是數字
    # if total.isdigit() == False:
    #    total = 0
    total = round(total,2)         # 小數點四捨五入到兩位
    label2Str.set("轉換後的台幣金額：" + str(total))


label1 = tk.Label(win,text="美金:",bg="#c1c0b9",font=20).place(x=20, y=60)

label2Str = tk.StringVar()
label2 = tk.Label(win,text="",bg="#c1c0b9",font=20,textvariable=label2Str).place(x=20, y=120)

entry1Str = tk.StringVar()
entry1 = tk.Entry(win,textvariable=entry1Str).place(x=80, y=60)

btn1 = tk.Button(win,text="轉換",command=event1,bg="#c1c0b9").place(x=250, y=60)

win.mainloop()                           # 最後步驟：程式做無限循環
