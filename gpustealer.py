### DESCRIBE METHODS TO BE CALLED
import os
import re
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
import bbywebsite as BB
from bbywebsite import *
import bbyemail as BBL
from bbyemail import *


class BestBuy_ripper(webdriver.Chrome):
    # cart_wait = WebDriverWait
    global timer
    timer = random.randrange(5.0, 8.0)
    global OS
    OS = os.name
    print(OS, 111111)

    chrome_options = Options

    def __init__(self, executable_path=r"/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/chromedriver", teardown=False):
        super(BestBuy_ripper, self).__init__()
        self.implicitly_wait(20)
        self.executable_path = executable_path
        os.environ['PATH'] += self.executable_path
        self.implicitly_wait(15)
        self.maximize_window()
        self.By = By
        self.Keys = Keys
        self.WebDriverWait = WebDriverWait
        self.Options = Options

    def install_plugins(self):
        pass
       # print(isinstance(chrome_options))
    def login(self):

        chrome_options = Options()
        chrome_options.add_extension(
            "/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/ad_blocker.crx")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        time.sleep(10)

        self.get(BB.URL)

        self.implicitly_wait(15)
        time.sleep(timer)
        print(OS)
        print('Random Wait Time', timer)
        time.sleep(3)


        nav_click = self.find_element_by_xpath('//*[@id="site-control-content"]')
        nav_click.click()


    def login_info(self):
        #self.get(BB.URL)
        nav_copy = self.find_element_by_xpath('//*[@id="site-control-content"]')
        nav_copy.click()

        nav_click00 = self.find_element_by_xpath(r'/html/body/div[2]/div/div/div[1]/header/div[2]/nav/ul/li[1]/div/button/span')
        nav_click00.click()
        print('1111')
        time.sleep(3)
        nav_click01 = self.find_element_by_xpath(r'/html/body/div[2]/div/div/div[1]/header/div[2]/nav/ul/li[1]/div/div/div/div[1]/div/div/div/div/div/a[1]')
        nav_click01.click()


        print('2222')
        time.sleep(3)

        email_login = self.find_element_by_id("fld-e")
        email_login.click()
        email_login.send_keys(BBL.ADDR)

        print('33333')
        pword_login = self.find_element_by_id("fld-p1")
        pword_login.click()
        print('4444444')


        final_click = self.find_element_by_xpath("/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/div/form/div[4]/button")
        final_click.click()

        print('555555555')

        pword_login.send_keys(BBL.PASS, Keys.ENTER)
        #pword_login.send


        time.sleep(5)


    def first_page(self):
        self.get(BB.URL01)
        print('Successfully Logged In')

    def iterate(self):
        try:
            time.sleep(2)
            ret = WebDriverWait(self, timer).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart-button")))
            ret.click()
            if ret.click():
                return 'True'

        except Exception as fail:
            print('error in checkout box iteration', str(fail))
            self.refresh()

    def click_thru_page(self):
        self.get("https://www.bestbuy.com/cart")

        checkoutBtn = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button")).click())

        if checkoutBtn == True:
            print("Successfully added to cart")


        ############ EMAIL FIELD ##############
        ############ EMAIL FIELD ##############
    def send_email(self): ## add email / password

        emailField = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e")).send_keys(bbyemail.ADDR))

        pwField = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1")).send_keys(bbyemail.PASS))

        signInBtn = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button")).click())

        print("Signing in")

        cvvField = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.ID, "credit-card-cvv"))
        )
        cvvField.send_keys(info.cvv)
        print("Attempting to place order")

        placeOrderBtn = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track").click())
        )


    def card_and_order(self):
        EC.presence_of_element_located((By.ID, "credit-card-cvv"))
        cvvField.send_keys(info.cvv)
        print("Attempting to place order")
        complete = false




