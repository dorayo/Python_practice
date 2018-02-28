#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from tkinter import *
import socket

class Application(Frame):
    def __init__(self, master=None, width=360, height=480):
        super().__init__(master)
        self.master = master
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.title('socket客户端程序')
        self.w = width
        self.h = height
        self.createWidgets()
        self.drawCenter()

        # 创建socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def createWidgets(self):
       Label(self.master, text='IP地址：').grid(row=0)
       Label(self.master, text='端口：').grid(row=1)
       self.ip_addr = StringVar(value='127.0.0.1')
       self.e_ip = Entry(self.master, textvariable=self.ip_addr)
       # self.e_ip.bind('<Button-1>', self.handleEvent)
       self.e_ip.grid(row=0, column=1, sticky=W)
       self.port = StringVar(value='9999')
       self.e_port = Entry(self.master, textvariable=self.port)
       self.e_port.grid(row=1, column=1, sticky=W)
       self.connBtn = Button(self.master, command=self.conn, width=10, height=1, text='连接')
       self.connBtn.grid(row=3, column=0, sticky=E)
       self.discBtn = Button(self.master, text='断开', command=self.disc, width=8, height=1)
       self.discBtn.grid(row=3, column=1)

       self.msgBox = Text(self.master, borderwidth=1, width=30, height=20, relief=GROOVE)
       self.msgBox.grid(row=4, columnspan=2)
       self.msgBox.config(state='normal')
       self.msgBox.insert(END, 'Messages from the server:\n')
       self.msgBox.config(state='disabled')

       # 添加滚动条
       self.scrollbar = Scrollbar(self.master) # height = not permitted here!
       self.scrollbar.config(command= self.msgBox.yview)
       self.scrollbar.grid(row=4, column=1, sticky=N+S+E)
       self.msgBox.config(yscrollcommand= self.scrollbar.set)

       self.smsg = StringVar()
       self.e_msg = Entry(self.master, textvariable=self.smsg, width=50)
       self.e_msg.grid(row=5, columnspan=2)
       self.sendBtn = Button(self.master, text='发送', command=self.sendMsg, width=10, heigh=1, )
       self.sendBtn.grid(row=6, column=0, sticky=SE)
       Button(self.master, text='退出', command=self.master.quit, width=8, heigh=1).grid(row=6, column=1, sticky=S)

    def drawCenter(self):
        sw = self.master.winfo_screenwidth() # 用户屏幕宽度
        sh = self.master.winfo_screenheight() # 用户屏幕高度
        x = int(sw/2 - self.w/2) # 距屏幕左边框的像素点数
        y = int(sh/2 - self.h/2) # 距屏幕上边框的像素点数
        # self.master.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))
        self.master.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    def handleEvent(self, event):
        print('event: %s' % event)

    def conn(self):
        ip_addr = self.e_ip.get()
        port = self.e_port.get()
        print('connecting to %s on port %s...' % (ip_addr, port))
        self.sock.connect((ip_addr, int(port)))
        self.recvMsg()

    def recvMsg(self):
        msg = self.sock.recv(1024).decode('utf-8')
        print('recv msg: %s' % msg)
        self.msgBox.config(state='normal')
        self.msgBox.insert(END, msg+'\n')
        self.msgBox.config(state='disabled')

    def disc(self):
        self.sock.close()
        print('disconnected from the server...')

    def sendMsg(self):
        smsg = self.smsg.get()
        self.sock.send(smsg.encode('utf-8'))
        print('send msg: %s' % smsg)
        self.recvMsg()

if __name__ == '__main__':
    app = Application(master=Tk())
    app.mainloop()
