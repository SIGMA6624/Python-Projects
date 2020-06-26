import requests


requests.get('https://automatetheboringstuff.com/files/rj.txt')
#<Response [200]>
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code
#200   #example: 404 is an error
len(res.text)
#178978
print(res.text[:500])
"""The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare



This eBook is for the use of anyone anywhere at no cost and with

almost no restrictions whatsoever.  You may copy it, give it away or

re-use it under the terms of the Project Gutenberg License included

with this eBook or online at www.gutenberg.org/license





Title: Romeo and Juliet



Author: William Shakespeare



Posting Date: May 25, 2012 [EBook #1112]

Release Date: November, 1997  [Etext #1112]



Language: Eng"""

res.raise_for_status()     #returning nothing means the operation was successfully carried out
badRes =  requests.get('https://automatetheboringstuff.com/dsffgsdgdfgsfsdf') #doesn't exist
badRes.raise_for_status()
#Traceback (most recent call last):
#  File "<pyshell#9>", line 1, in <module>
#    badRes.raise_for_status()
#  File "C:\Users\Dell\AppData\Local\Programs\Python\Python38\lib\site-packages\requests\models.py", line 941, in raise_for_status
#    raise HTTPError(http_error_msg, response=self)
#requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://automatetheboringstuff.com/dsffgsdgdfgsfsdf

playFile = open('RomeoandJuliet.txt', 'wb') #for this case, use 'wb' meaning write binary. 
for chunk in res.iter_content(100000):   #res.iter_content(x); x is the number of bytes to write per iteration
    playFile.write(chunk)
#100000
#78978
playFile.close()

#when I ran this, os.getcwd() is 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python38'.
#Though, I placed this at 'D:\Documents\Hobby\Automate the Boring Stuff With Python'

#to read more about the request module, go to: https://requests.readthedocs.io/en/latest/
