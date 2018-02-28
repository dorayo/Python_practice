#!/usr/bin/env python3

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Helo, world!')
        self.helloLabel.pack()

        self.nameInput = Entry(self)
        self.nameInput.pack()

        self.alertBtn = Button(self, text='Hello', command=self.hello)
        self.alertBtn.pack()

        self.quitBtn = Button(self, text='Quit', command=self.quit)
        self.quitBtn.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello %s' % name)
root = Tk()
app = Application(master=root)
# 设置窗口标题
app.master.title('Hello, world')
# 主消息循环
app.mainloop()
