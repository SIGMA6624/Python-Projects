#draw a rectangular spiral on MS Paint
import pyautogui

pyautogui.click()    #click to put drawing program in focus. Place mouse at MS Paint.
distance = 200
duration = 1

while distance > 0:
    print(distance,0)
    pyautogui.dragRel(distance, 0, duration = duration)   #move right
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration = duration)   #move down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration = duration)  #move left
    distance = distance -25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration = duration)   #move up


#Note: PyAutoGUI has a fail-safe mechanism to keep the program from going on forever. 
#If you forcibly move your mouse to a corner of the screen, PyAutoGUI will forcibly shut down the program.
