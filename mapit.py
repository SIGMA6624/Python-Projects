import webbrowser, sys, pyperclip
#This script was saved in C:\Users\Dell\MyPythonScripts. A batch file was also made to run it from window+r.

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']  what you get if you typed in windows+r: mapit.py, 870 Valencia St.

# Check if command line arguments were passed
if len(sys.argv) > 1: # the length of the list is just 1 if no arguments are passed
    #This is the output: ['mapit.py', '870', 'Valencia', 'St.']
    #We want this: '870 Valencia St.
    address = ' '.join(sys.argv[1:])
    
else: #if no arguments, assume it's on the clipboard
    address = pyperclip.paste()

#https://www.google.com/maps/place/870+Valencia+St,+San+Francisco,+CA+94110,+USA/@37.6793864,-123.044079,8.92z/data=!4m5!3m4!1s0x808f7e3dae0fc797:0x26acf7c8a5797e94!8m2!3d37.7589579!4d-122.4216627
#https://www.google.com/maps/place/<ADDRESS>
#^After some trial and error, we find out that you can just type normally at <ADDRESS> to arrive at the same place.
webbrowser.open('https://www.google.com/maps/place/' + address)
