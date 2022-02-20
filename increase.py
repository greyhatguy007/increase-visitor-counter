from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

print()
print("Made with \u2764\uFE0F From Ritvik")
print()

user = input("ENTER YOUR GITHUB USERNAME :")
count = int(input("ENTER NUMBER OF VISITOR COUNTS TO INCREASE : "))
url = "https://github.com/"+user+"/"+user+"/"
print("HANG ON, THIS MIGHT TAKE A BIT...")
print("GO GRAB A COFFEE !")

browser = webdriver.Chrome(options=options)


for _1 in range(0,count):
    browser.get(url)
    print((_i+1)*100/(count), " PERCENT DONE")
browser.close()
