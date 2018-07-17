#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
import tkinter.font

# 创建主窗口
root = tkinter.Tk()
root.title("小姐姐我要撩你")


def center_window(w, h):
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


center_window(480, 320)

ft = tkinter.font.Font(family='微软雅黑', size=20, weight=tkinter.font.BOLD)
ft2 = tkinter.font.Font(family='微软雅黑', size=30, weight=tkinter.font.BOLD)

# 创建标签
tkinter.Label(root, text="").pack()
tkinter.Label(root, text="小姐姐，我观察你很久了", font=ft).pack()
tkinter.Label(root, text="做我女朋友好不好?", font=ft2, foreground="#FF0000").pack()

text = "房产证上写你名！ 保大！ 我妈会游泳！ 拒绝我？不存在的！"
lines = text.split(" ")
print(lines)

i = 0


def nocmd():
    global i
    tkinter.messagebox.showinfo('提示', lines[i])
    i += 1
    if i == len(lines):
        no.configure(state='disabled')


def yescmd():
    tkinter.messagebox.showinfo('提示', "3号目标已拿下！")


tkinter.Label(root, text="").pack()
# 创建按钮并把命令绑定到弹框
yes = tkinter.Button(root, text="好", font=ft, command=yescmd).pack()
tkinter.Label(root, text="").pack()
# 创建按钮并把命令绑定到退出
no = tkinter.Button(root, text="不好", font=ft, command=nocmd)
no.pack()
# 启动主循环
root.mainloop()
