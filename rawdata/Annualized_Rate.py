

# author:LSQ
# e-mail:546397641@qq.com
# date:2022.07.03

import tkinter as tk
from tkinter import *

'''说明
年化率和收益转换计算
'''


def quit():
    root.destroy()

def calculateA():
    capital = float(entry0.get())
    monthValue = int(entry1.get())
    annualRate = float(entry2.get())
    value = float((10000*(annualRate/100)/360) * (capital/10000) * monthValue * 30)
    entry3.set(round(value,3))

def calculateB():
    capital = float(entry00.get())
    monthValue = int(entry11.get())
    profitValue = float(entry22.get())
    value = profitValue/(monthValue * 30) / (capital/10000) * 360/10000 * 100
    entry33.set(round(value,3))

root = tk.Tk()
root.title('HOME')
root.geometry('400x200')  # 窗口长x窗口高
frame_show = Frame(width=800,height=400,bg="#008080")
img0 = PhotoImage(file='split.png')  # 图片
Lable1=tk.Label(root, image=img0).place(x=190,y=40)

LableTitle0=tk.Label(root,text='年化率 与 收益 转换器 v.1.3',width=40,height=1).place(x=60,y=0)


# ---1
entry0 = tk.StringVar()
# entry0.set('请输入数字')  #文本框中默认的信息
# place是插件坐标
Lable0=tk.Label(root,text='本金',width=8,height=1).place(x=0,y=40)
Entry0 = tk.Entry(root,textvariable=entry0,width=10).place(x=60,y=40)
Lable0a=tk.Label(root,text='元',width=2,height=1).place(x=140,y=40)

entry1 = tk.StringVar()
# entry1.set('请输入数字')
Lable1=tk.Label(root,text='月数',width=8,height=1).place(x=0,y=70)
Entry1 = tk.Entry(root,textvariable=entry1,width=10).place(x=60,y=70)
Lable1a=tk.Label(root,text='个',width=2,height=1).place(x=140,y=70)

entry2 = tk.StringVar()
# entry1.set('请输入数字')
Lable2=tk.Label(root,text='年化率',width=8,height=1).place(x=0,y=100)
Entry2 = tk.Entry(root,textvariable=entry2,width=10).place(x=60,y=100)
Lable22=tk.Label(root,text='%',width=2,height=1).place(x=140,y=100)

entry3 = tk.StringVar()
# entry3.set('请输入数字')
Lable3=tk.Label(root,text='收益',width=8,height=1).place(x=0,y=130)
Lable3a = tk.Label(root,textvariable=entry3,width=10).place(x=60,y=130)
Lable3b=tk.Label(root,text='元',width=2,height=1).place(x=140,y=130)

Button0 = tk.Button(root,text='转换A',width=5,height=1,command=calculateA).place(x=60,y=160)

# ---2
entry00 = tk.StringVar()
# entry0.set('请输入数字')  #文本框中默认的信息
# place是插件坐标
Lable00=tk.Label(root,text='本金',width=8,height=1).place(x=210,y=40)
Entry00 = tk.Entry(root,textvariable=entry00,width=10).place(x=270,y=40)
Lable00a = tk.Label(root,text='元',width=2,height=1).place(x=350,y=40)

entry11 = tk.StringVar()
# entry1.set('请输入数字')
Lable11=tk.Label(root,text='月数',width=8,height=1).place(x=210,y=70)
Entry11 = tk.Entry(root,textvariable=entry11,width=10).place(x=270,y=70)
Lable11a = tk.Label(root,text='个',width=2,height=1).place(x=350,y=70)

entry22 = tk.StringVar()
# entry1.set('请输入数字')
Lable22=tk.Label(root,text='收益',width=8,height=1).place(x=210,y=100)
Entry22 = tk.Entry(root,textvariable=entry22,width=10).place(x=270,y=100)
Lable22a =tk.Label(root,text='元',width=2,height=1).place(x=350,y=100)

entry33 = tk.StringVar()
# entry1.set('请输入数字')
Lable33=tk.Label(root,text='年化率',width=8,height=1).place(x=210,y=130)
Lable33a = tk.Label(root,textvariable=entry33,width=10).place(x=270,y=130)
Lable33b = tk.Label(root,text='%',width=2,height=1).place(x=350,y=130)

Button1 = tk.Button(root,text='转换B',width=5,height=1,command=calculateB).place(x=270,y=160)

# ---3
Button2 = tk.Button(root,text='退出',width=5,height=1,command=quit).place(x=170,y=160)


root.mainloop()

