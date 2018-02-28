#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from tkinter import *

class Application(Frame):
    def __init__(self, master=None, width=360, height=128):
        super().__init__(master)
        self.master = master
        self.master.title('抛硬币概率实验')
        self.w = width
        self.h = height
        self.createWidgets()
        self.drawCenter()

    def createWidgets(self):
       Label(self.master, text='实验次数：').grid(row=0, sticky=E)
       Label(self.master, text='正面出现的次数：').grid(row=1, sticky=E)
       Label(self.master, text='出现正面概率：').grid(row=2, sticky=E)
       self.e1 = Entry(self.master)
       self.e1.bind('<Button-1>', self.handleEvent)
       self.e1.insert(END, '请输入实验次数：<eg:100>')
       self.e1.grid(row=0, column=1)
       self.count = StringVar(value='0')
       self.e2 = Entry(self.master, textvariable=self.count, state='disabled')
       self.e2.grid(row=1, column=1)
       self.p = StringVar(value='0')
       self.e3 = Entry(self.master, textvariable=self.p, state='disabled')
       self.e3.grid(row=2, column=1)
       self.runBtn = Button(self.master, command=self.click, width=3, height=1, text='运行')
       self.runBtn.grid(row=3, column=0, sticky=E)
       Button(self.master, text='关闭窗口', command=self.master.quit, width=8, height=1).grid(row=3, column=1)

    def drawCenter(self):
        sw = self.master.winfo_screenwidth() # 用户屏幕宽度
        sh = self.master.winfo_screenheight() # 用户屏幕高度
        x = int(sw/2 - self.w/2) # 距屏幕左边框的像素点数
        y = int(sh/2 - self.h/2) # 距屏幕上边框的像素点数
        # self.master.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))
        self.master.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))
        
    def handleEvent(self, event):
        print('event: %s' % event)
        self.e1.delete(0, END)
        
    def click(self):
        print('running...')
        pc = 0 # 正面次数
        allcount = 0
        count = int(self.e1.get() or '0')
        if count > 0:
            for i in range(count):
                num = random.randint(0,1)
                if num == 0:
                    pc = pc + 1
                self.count.set(str(pc)) # 设置正面次数
                self.p.set(str(pc/count)) # 设置正面概率


if __name__ == '__main__':
    app = Application(master=Tk())
    app.mainloop()
