import pyautogui
import time

for i in range(1,10+1):
    foto=pyautogui.screenshot()
    time.sleep(4)
    foto.save('foto1%d .png'%(i))
    print('Working %d'%(i))
print('Worked')