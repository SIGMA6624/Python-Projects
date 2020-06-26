import pyautogui
#The screen looked like this while doing this in Python IDLE: D:\Documents\Hobby\Automate the Boring Stuff With Python\Screenshots\screenshots_and_image_recognition_screen.png

pyautogui.screenshot()
#<PIL.Image.Image image mode=RGB size=1920x1080 at 0x1C376BF0CD0>
pyautogui.screenshot('D:\Documents\Hobby\Automate the Boring Stuff With Python\Screenshots\screenshot_example.png')   #saves screenshot to the file 
#<PIL.Image.Image image mode=RGB size=1920x1080 at 0x1C376C44850>

pyautogui.locateOnScreen('D:\Documents\Hobby\Automate the Boring Stuff With Python\Screenshots\calc7key.png')       #you can search your screen to match a picture from your picture directory. Just be careful that your picture needs to be EXACT to the spot you want to match. 
#Box(left=1276, top=537, width=94, height=53)       #gets the top left part of the match. Also says the width and height of the match.
pyautogui.locateCenterOnScreen('D:\Documents\Hobby\Automate the Boring Stuff With Python\Screenshots\calc7key.png')
#Point(x=1323, y=563)                               #gets the center part of the match.
pyautogui.moveTo((1323,563), duration = 1)          #goes to the '7' key of the calculator
pyautogui.click((1323,563))                         #click te '7' key of the calculator.
pyautogui.click(1323,563)                           #another way to do the prev line.


#Al Sweigart demonstrates the potential of screenshots and image recognition by playing Sushi Go Round with just Python: https://github.com/asweigart/sushigoroundbot
