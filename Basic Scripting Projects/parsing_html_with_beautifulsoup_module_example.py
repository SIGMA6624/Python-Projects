import bs4, requests

def getAmazonPrice(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    #headers is just a way for your scraping program to be shown as a browser, according to forums. Apparently, this is used because websites like Amazon have anti-scraping measures. 
    #To find what headers to use: https://www.whatismybrowser.com/detect/what-is-my-user-agent
    
    res = requests.get(productUrl, headers = headers)
    res.raise_for_status()  #returns an error if not successful
    
    soup1 = bs4.BeautifulSoup(res.text, 'html.parser')
    soup2 = bs4.BeautifulSoup(soup1.prettify(), "html.parser")
    #^soup2 isn't exactly shown in the tutorial, but it was suggested to get around Amazon's anti-scraping measures. Other websites aren't strict, so try just using soup1 if it works. This program was written at 4/17/2020.
    
    elems = soup2.select('#unqualifiedBuyBox > div > div.a-text-center.a-spacing-mini > span')
    #Since we don't have 'Copy CSS Path', use 'Copy Selector'.
    #print(elems)
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
print('The price is ' + price)

#recommended websites to scrape: weather
