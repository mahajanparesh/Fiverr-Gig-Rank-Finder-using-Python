from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

status = False
page = 1
bLink = "https://www.fiverr.com/"
keyword = "montage editor"
gig = ""
userName = "haroon_pro"
browser = webdriver.Opera(executable_path='C:/Users/Paresh Mahajan/AppData/Local/Programs/Python/Python39/operadriver.exe')
browser.maximize_window()

# connect to the specific URL
browser.get(bLink)
time.sleep(3)

def typeText():
    time.sleep(1)
    textInput = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/form/input')
    textInput.send_keys(keyword)
    submitBtn = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/form/button')
    submitBtn.click()

def checkText():
    try:
        result = browser.page_source.__contains__(userName)
        return result
    except:
        error()

def nextButton():
    try:

        link = browser.find_element_by_xpath('//*[@id="pagination"]/li[12]/a')
        link.click()
        time.sleep(4)
    except:
        error()

def error():
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    nextButton()

typeText()
while True:
    status = checkText()
    if (status == True):
        print("Found At Page No.: ",page)
        break
    else:
        nextButton()
        page += 1


