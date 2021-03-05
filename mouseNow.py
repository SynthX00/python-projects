#! python 3
#mouseNow.py - Dispalys the mouse cursor's current position.
import pyautogui

print('Press Ctrl-C to quit.')

try:
    while True:
        #Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)}'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')