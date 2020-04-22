from selenium import webdriver
#Need to manually install selenium
#To open Firefox, download geckodriver: https://github.com/mozilla/geckodriver/releases
#To open Chrome, download chromedriver (please pay attention to your Chrome version number and download the same version number for chromedriver): https://sites.google.com/a/chromium.org/chromedriver/home

#browser = webdriver.Firefox()  #this now works. Maybe I need to restart the computer aftr downloading geckodriver and placing it on the PATH environment variable.
browser = webdriver.Chrome()
#I made a path environment variable linking to C:\Users\Dell\AppData\Local\Programs\Python\Python38, where my geckodriver and chromedriver applications are saved.
#If you don't do this, you need to place the absolute filename in those parentheses.
#DO NOT CLOSE the geckodriver/ chromedriver window that pops up when running the program.


#Example goal: search 'scholarship' on the DLSU website and return results on Chrome.
browser= webdriver.Chrome()
browser.get('https://www.dlsu.edu.ph/search_gcse/?q=')
searchElem = browser.find_element_by_id('gsc-i-id3')   #ALWAYS run this before using send_keys
searchElem.send_keys('scholarship')
#the submit() function didn't work in the DLSU website. So I have to resort to clicking the search button.
submitButton = browser.find_element_by_css_selector('#___gcse_2 > div > div > form > table > tbody > tr > td.gsc-search-button > button')    
submitButton.click()

browser.back()      #previous page
browser.forward()   #next page
browser.refresh()   #refresh
browser.quit()      #close browser
