import pyautogui
import time
import random
#
# #妖气封印函数
# def yaoqi():
# 	#点击组队
# 		pyautogui.moveTo(424,904)
# 	pyautogui.click()
# 	time.sleep(2)
# 	#点击妖气封印
# 	pyautogui.moveTo(433,852)
# 	pyautogui.click()
# 	time.sleep(2)
# 	start=time.clock()
# 	while(True):
# 		end=time.clock()
# 		#刷新、加入，准备
# 		pyautogui.moveTo(1116,907)
# 		pyautogui.click()
# 		time.sleep(0.1)
# 		pyautogui.moveTo(1538,330)
# 		pyautogui.click()
# 		pyautogui.moveTo(1668,806)
# 		pyautogui.click()
# 		#判断运行时长
# 		if int(end-start)==600:
# 			break
#
#
# #天雷鼓函数
#
# def Tianlei():
# 	#点击组队
# 	pyautogui.moveTo(424,904)
# 	pyautogui.click()
# 	time.sleep(2)
# 	#点击天雷鼓
# 	pyautogui.moveTo(466,639)
# 	pyautogui.click()
# 	time.sleep(2)
# 	start=time.clock()
# 	while(True):
# 		end=time.clock()
# 		#刷新、加入，准备
# 		pyautogui.moveTo(1116,907)
# 		pyautogui.click()
# 		time.sleep(0.1)
# 		pyautogui.moveTo(1538,330)
# 		pyautogui.click()
# 		pyautogui.moveTo(1668,806)
# 		pyautogui.click()
# 		#判断运行时长
# 		if int(end-start)==600:
# 			break
#
#


def yuhun():
 #点击组队
 x_move = random.randint(1090, 1250)
 y_move = random.randint(630,700)
 t_rand = random.randint(30,40)
 count = 1
 while (count<10):
   pyautogui.moveTo(x_move,y_move)
   pyautogui.click()
   time.sleep(t_rand)
   pyautogui.click()
   t_rand2 = random.randint(1,2)
   pyautogui.click()
   count=count+1
   print("n=",count)



if __name__ == '__main__':
   yuhun()