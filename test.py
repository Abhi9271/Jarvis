# import name
#import random
# import psutil
# import winsound
# from win10toast import ToastNotifier
# import pyautogui as pa
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Edge('C:/bin/msedgedriver.exe')
# driver.get("www.google.co.in")
# time.sleep(5)
# driver.close()


# pa.PAUSE = 1.5
# import os
# def closeFile():
#     try:
#         os.system('TASKKILL /F /IM msedge.exe')
#     except Exception as e:
#         print(e)

# if __name__ == "__main__":
#     closeFile()

# f = open('creds.txt','w')
# id = "iamjarvis3000@gmail.com\n"
# pw = "Vibranium2193"
# f.writelines([id, pw])
# f.close()

# fr = open('creds.txt')
# eid = ""
# pw = ""
# if fr.mode == 'r':
#     r = fr.readlines()
#     eid = r[0]
#     pw = r[1]
#     print(eid)
#     print(pw)

#     fr.close()
# else:
#     print('File not in read mode')
# def checkIfProcessRunning(processName):
#     '''
#     Check if there is any running process that contains the given name processName.
#     '''
#     #Iterate over the all the running process
#     for proc in psutil.process_iter():
#         try:
#             # Check if process name contains the given name string.
#             if processName.lower() in proc.name().lower():
#                 return True
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#     return False

# if __name__ == "__main__":
# winsound.MessageBeep()
# winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
# winsound.PlaySound("SystemDefault", winsound.SND_ALIAS)
#     if checkIfProcessRunning('msedge'):
#         print('Yes an edge process is running')
#     else:
#         print('No process is running')
# toaster = ToastNotifier()
# toaster.show_toast(title="Sample Notification",msg="Python is awesome!!!")
# distance = 200
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.5)   # move right
#     distance -= 5
#     pyautogui.drag(0, distance, duration=0.5)   # move down
#     pyautogui.drag(-distance, 0, duration=0.5)  # move left
#     distance -= 5
#     pyautogui.drag(0, -distance, duration=0.5)  # move up
# pos = pa.position()
# print(pos)
# pa.hotkey('altleft', 'tab')
# pa.moveTo(1340,6)
# pa.click()
# pa.moveTo(683,384)

# f = open('myself.txt', mode='r')
# count = len(open('myself.txt').readlines())
# r = f.readlines()
# rd = random.randint(0, count-1)
# print(r[rd])
