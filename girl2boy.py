#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入sys和tkinter模块
import tkinter
import tkinter.messagebox
import tkinter.font
from PIL import Image, ImageTk

# 创建主窗口
root = tkinter.Tk()
root.title("来自未知世界的小姐姐")


# root.minsize(600, 400)

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
tkinter.Label(root, text="小哥哥，我观察你很久了", font=ft).pack()
tkinter.Label(root, text="做我男朋友好不好?", font=ft2, foreground="#FF0000").pack()

text = "我喜欢你 我知道你在等我这一句话 请你不要拒绝我 拒绝我？不存在的"
lines = text.split(" ")
print(lines)

i = 0


def nocmd():
    global i
    tkinter.messagebox.showinfo('提示', lines[i])
    i += 1
    if i == len(lines):
        no.configure(state='disabled')


def show():
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    image = Image.open('resources/3.gif')
    w, h = image.size

    if ws < w or hs < h:
        image = image.resize((w // 2, h // 2))
        w, h = image.size

    top1 = tkinter.Toplevel()
    top1.title("相公，我来了！")
    img = ImageTk.PhotoImage(image)

    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    print(w, h, x, y)
    top1.geometry('%dx%d+%d+%d' % (w, h, x, y))

    canvas = tkinter.Canvas(top1, width=image.width, height=image.height, bg='white')
    canvas.pack()

    canvas.create_image(0, 0, image=img, anchor="nw")
    top1.mainloop()


def yescmd():
    if tkinter.messagebox.askyesno("你终于来了", "跟我走吧？"):
        show()
    else:
        show()


tkinter.Label(root, text="").pack()
# 创建按钮并把命令绑定到弹框
yes = tkinter.Button(root, text="好",font=ft, command=yescmd).pack()
tkinter.Label(root, text="").pack()
# 创建按钮并把命令绑定到退出
no = tkinter.Button(root, text="不好", font=ft, command=nocmd)
no.pack()
# 启动主循环
root.mainloop()
