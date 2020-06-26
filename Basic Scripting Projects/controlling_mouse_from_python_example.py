import pyautogui
#pip install pyautogui
#documentation: https://pyautogui.readthedoc.org

#x is left(-) and right(+). y is up(-) and down(+).
pyautogui.size()
Size(width=1920, height=1080)
width, height = pyautogui.size()
width
#1920
height
#1080

#putting the mouse pointer in 3 random positions while running pyautogui.position()
pyautogui.position()
#Point(x=1484, y=266)
pyautogui.position()
#Point(x=372, y=616)
pyautogui.position()
#Point(x=1237, y=895)

pyautogui.moveTo(10,10)                    #mouse teleports to upper left of the screen.
pyautogui.moveTo(10,10, duration = 1.5)    #mouse moves to upper left of the screen in 1.5 s.

pyautogui.moveRel(200,0)                   #move the mouse pointer 200 pixels right relative to the current position
pyautogui.moveRel(200,0, duration = 2)
pyautogui.moveRel(0,-100)                  #move the mouse pointer 100 pixels up relative to the current position
pyautogui.moveRel(0,-100, duration = 1)

pyautogui.click(1296, 49)                  #click at the 'Help' button at the Python IDLE
pyautogui.click()                          #click at the current position of the mouse pointer

"""
To prevent from using pyautogui.position(), a simple way to track mouse position real-time:
-Go to cmd
-type: py -3.8      #or whatever version you have
-type: import pyautogui
-type: pyautogui.displayMousePositon()

You will now be able to see the mouse position in real time in the command prompt.
This will not look good at the Python IDLE, as it prints a new line every time an update happens.
"""
