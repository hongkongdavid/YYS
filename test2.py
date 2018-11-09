
import time

import win32gui, win32ui, win32con, win32api

from ctypes import *

import cv2

import numpy as np

import random


def clickLeftCur():  # 单击

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def moveCurPos(x, y):  # 移动鼠标

    windll.user32.SetCursorPos(x, y)


def getCurPos():  # 获得鼠标位置信息，这个再实际代码没用上，调试用得上

    return win32gui.GetCursorPos()






def window_capture(filename):

    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口

    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）

    hwndDC = win32gui.GetWindowDC(hwnd)

    # 根据窗口的DC获取mfcDC

    mfcDC = win32ui.CreateDCFromHandle(hwndDC)

    # mfcDC创建可兼容的DC

    saveDC = mfcDC.CreateCompatibleDC()

    # 创建bigmap准备保存图片

    saveBitMap = win32ui.CreateBitmap()

    # 获取监控器信息

    MoniterDev = win32api.EnumDisplayMonitors(None, None)

    w = MoniterDev[0][2][2]

    h = MoniterDev[0][2][3]

    # print w,h　　　#图片大小

    # 为bitmap开辟空间

    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    # 高度saveDC，将截图保存到saveBitmap中

    saveDC.SelectObject(saveBitMap)

    # 截取从左上角（0，0）长宽为（w，h）的图片

    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)

    saveBitMap.SaveBitmapFile(saveDC, filename)




filename = "blackground.jpg"#储存的文件名

while True:

    time.sleep(2)#设置隔2秒运行一次

    #截图

    window_capture(filename)#对整个屏幕截图，并保存截图为filename

    #原图

    srcImg = cv2.imread(filename)#读取filename的截图文件，这里应该是可以对截图函数进行修改，不用产生中间的文件，截图直接与ndarray形式存在

    begin = cv2.imread('begin.png')#读取点击开始战斗的 标准图像

    end1 = cv2.imread('end1.png')#结束之后点击屏幕任意位置，开宝箱

    end2 = cv2.imread('end2.png')#开完宝箱后，点击任意结束本轮


