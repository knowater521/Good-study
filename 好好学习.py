from ctypes import *
from time import sleep
import sys
import ctypes
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def getTime():
    while (True):
        min = input('输入分钟:')
        mills = input('秒数:')
        # 判断是否都输入了数字
        if (min.isdigit() and mills.isdigit()):
            break;
    totalTime = int(min) * 60 + int(mills)
    print(totalTime)
    return totalTime
def daojishi(t):
    for i in range(t):
        print('%d分%d秒' % (t / 60, t % 60))
        sleep(1)
        t -= 1

if is_admin():
 user32 = windll.LoadLibrary('C:\\Windows\\System32\\user32.dll')
 t=getTime() #获取锁机时间
 user32.BlockInput(True);  #锁定键盘、鼠标
 print('好好学习，天天向上！')
 print("先别玩电脑了吧 |･ω･｀)")
 daojishi(t)#锁机
 user32.BlockInput(False);
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

