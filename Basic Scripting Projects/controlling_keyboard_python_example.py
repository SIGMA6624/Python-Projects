import pyautogui

#Setup: Python IDLE on right side, Notepad on left side
#in IDLE to run 2 commands: pyautogui.click(200,200); pyautogui.typewrite('Hello world!')
pyautogui.click(200,200)
pyautogui.typewrite('Hello world!')                     #type 'Hello World' at current window instantly.
pyautogui.click(200,200)
pyautogui.typewrite('Hello world!', interval = 0.2)     #type 'Hello World' at current window with 0.2 seconds in between each keypress.
pyautogui.click(200,200)
pyautogui.typewrite(['a','b','left','left','X','Y'], interval = 1)   #individually type buttons a certain order with a certain interval.
pyautogui.KEYBOARD_KEYS
"""
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',
 ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';',
 '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e',
 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft',
 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward',
 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide',
 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13',
 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3',
 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help',
 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert',
 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9',
 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack',
 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock',
 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop',
 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft',
 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']
 """

pyautogui.press('f1')             #In Python IDLE, open Python documentation.
pyautogui.hotkey('ctrl', 'o')     #hotkey allows for keyboard shortcuts. This allows "Open a new file" in Python IDLE.
