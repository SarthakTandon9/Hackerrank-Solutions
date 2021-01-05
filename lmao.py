from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from random import randrange
import time
#importing the necessary stuff. 

refresh_rate = 10
#setting the refesh rate, the lower it is, the faster the views go up. 
browser = []
browser1 = webdriver.Chrome(ChromeDriverManager().install())
browser2 = webdriver.Chrome(ChromeDriverManager().install())
browser3 = webdriver.Chrome(ChromeDriverManager().install())
#making three browser instances, you can make as many as your computer can support. 

browser.append(browser1)
browser.append(browser2)
browser.append(browser3)
#adding the instances to the browser list. 

for i in browser:
    i.get("Add your link here.")
#opening the desired link in all of the browser instances. 
while(True):
    browser_num = randrange(0, len(browser))
    #choosing a random browser to refresh.
    browser[browser_num].refresh()
    #refreshing the browser.
    print(browser_num, " has been refreshed.")
    time.sleep(refresh_rate)
    


