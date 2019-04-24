# coding=utf-8
import numpy as np
from tkinter import *
from collections import Counter

# 创建出窗口
window = Tk()
window.title("相亲配对")
window.geometry('400x250')

# 对窗口进行表格式布局
Label(window, text = '每年出差/旅行的公里数:').grid(row = 0, column = 0)
Label(window, text = '玩游戏消耗时间的百分比:').grid(row = 1, column = 0)
Label(window, text = '每周消费的冷饮公升数:').grid(row = 2, column = 0)

# 设置用户的输入变量
t_0 = StringVar()
t_1 = StringVar()
t_2 = StringVar()

# 储存输入内容，并设置输入框格式
t0 = Entry(window, textvariable = t_0)
t1 = Entry(window, textvariable = t_1)
t2 = Entry(window, textvariable = t_2)
t0.grid(row = 0, column = 1, padx = 10, pady = 5)
t1.grid(row = 1, column = 1, padx = 10, pady = 5)
t2.grid(row = 2, column = 1, padx = 10, pady = 5)

# 接收到用户输入后，用K-近邻算法判断好感程度
def show():
    k_j = []
    user_date = np.array([float(t0.get()), float(t1.get()), float(t2.get())])
    with open('datingTestSet.txt') as info:
        for i in info.readlines():
            infos = i.split('\t')
            date = np.array([float(infos[0]), float(infos[1]), float(infos[1])])
            s = np.sqrt(np.sum(np.square(date-user_date)))
            if len(k_j) < 10:
                k_j.append([infos[3], s])
            else:
                for j in k_j:
                    if s < j[1]:
                        k_j.remove(j)
                        k_j.append([infos[3], s])
                        break
    print(k_j)
    text = []
    for k in k_j:
        if k[0][0] == "l":
            text.append("哇！恭喜你，缘分到来了，你极有吸引力哦！好好发展吧！！")
        elif k[0][0] == "s":
            text.append("哇！你有希望，虽然你的吸引力一般，但仍然是存在希望的！")
        else:
            text.append("额，不是你不够优秀，只是你选错了对象而已，换一个试试吧")
    Label(window, text = Counter(text).most_common(1)[0][0][:12]).grid(row = 6, column = 0)
    Label(window, text = Counter(text).most_common(1)[0][0][12:]).grid(row = 6, column = 1)


# 在窗口底部显示一个按键用于让用户提交，还有一个让用户退出的按键
Button(window, text='提交', width = 10, command = show).grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
Button(window, text = '溜了', width = 10, command = window.quit).grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)

# 显示出窗口
window.mainloop()
