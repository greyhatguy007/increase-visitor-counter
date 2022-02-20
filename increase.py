import time
start = time.time()
from math import ceil, floor
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

print()
print()
print("Made with \u2764\uFE0F From Ritvik")
print()

user = input("ENTER YOUR GITHUB USERNAME :")
count = int(input("ENTER NUMBER OF VISITOR COUNTS TO INCREASE : "))
url = "https://github.com/"+user+"/"+user+"/"

opt = input("DO YOU WISH TO ENABLE THREADING ? (Y/N) : ")
opt = opt.strip().upper()

if opt=="Y":
    print()
    print("NOTE : DON'T GIVE HIGH THREADS, POTATO PC'S WILL FRY")
    threads = int(input("ENTER NUMBER OF THREADS ( 2-5 RECOMMENDED): "))
    count = int(count/threads)
    browsers = []

    print("HANG ON, THIS MIGHT TAKE A BIT...")
    print("GO GRAB A COFFEE !")

    for _i in range(1,threads+1):
        temp = "browser"+str(_i)
        temp = webdriver.Chrome(options=options)
        #temp = webdriver.Chrome()
        browsers.append(temp)

    for _i in range(0,count):
        for browser in browsers:
            browser.get(url)
        print(round((_i+1)*100/(count),2), " PERCENT DONE")

    for browser in browsers:
        browser.close()

elif opt=='N':
    print("HANG ON, THIS MIGHT TAKE A BIT...")
    print("GO GRAB A COFFEE !")

    browser = webdriver.Chrome(options=options)


    for _i in range(0,count):
        browser.get(url)
        print(round((_i+1)*100/(count),2), " PERCENT DONE")
    browser.close()
else:
    print("INVALID CHOICE")
end = time.time()

print("PROCESS FINISHED, TIME TAKEN :", end-start)
print()
