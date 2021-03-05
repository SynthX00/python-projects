import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

#print(pyautogui.size())
#width, height = pyautogui.size()

#for i in range(10):
#        pyautogui.moveTo(100,100,duration=.25)
#        pyautogui.moveTo(200,100,duration=.25)
#        pyautogui.moveTo(200,200,duration=.25)
#        pyautogui.moveTo(100,200,duration=.25)

#for i in range(3):
#        pyautogui.moveRel(100,0,duration=.25)
#        pyautogui.moveRel(0,100,duration=.25)
#        pyautogui.moveRel(-100,0,duration=.25)
#        pyautogui.moveRel(0,-100,duration=.25)
#

buttonLocation = pyautogui.locateOnScreen('calc7.jpg', confidence=0.1)
print(buttonLocation)