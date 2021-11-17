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
from os import open

class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"
###########
color = Colors()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset




class Prettify():

    class Spinner:
        busy = False
        delay = 0.1

        @staticmethod
        def spinning_cursor():
            while 1:
                for cursor in '|/-\\': yield cursor

        def __init__(self, delay=None):
            self.spinner_generator = self.spinning_cursor()
            if delay and float(delay): self.delay = delay

        def spinner_task(self):
            while self.busy:
                sys.stdout.write(next(self.spinner_generator))
                sys.stdout.flush()
                time.sleep(self.delay)
                sys.stdout.write('\b')
                sys.stdout.flush()

        def __enter__(self):
            self.busy = True
            threading.Thread(target=self.spinner_task).start()

        def __exit__(self, exception, value, tb):
            self.busy = False
            time.sleep(self.delay)
            if exception is not None:
                return False

    def __init__(self):
       # self = self
        self.spinner = self.Spinner()


    def spinner(self):
        spinner = self.Spinner()
        return spinner

    def display_header(self):
        # print('*' * 75)
        color_red = Colors()
        global red0
        red0 = color_red.fgRed
        global reset0
        reset0 = color_red.reset

        x = 'x'
        print(f"{'X' * 125:^70}")
        print(f"{'X' * 125:^70}")
        pretty = f'{red0}xxx FILE-MOVER xxx{reset0}'.center(width)
        print(f'{pretty : ^70}')
        print(f"{'X' * 125: ^70}")

        one = (
            f'[USAGE] - [1] This is a python program that takes a specified file names, and moves them into an individual folder.')
        two = (
            f'[USAGE] - [2] The program works well with most download repositories, and currently gets around security measure implimented by \n[USAGE] - [2]b 1337x.to, itorrent && archive.org')
        three = (
            f'[USAGE] - [3] Download a LINK GRABBING extension from chrome, to pull the URLs off of the browsers tabs.')
        four = (f'[USAGE] - [4] Save the list into download_list.txt (Found in the Directory as this program')
        five = (
            f'[USAGE] - [5] Wait for downloads. Archive.org may be slow. The program saves both a LIST and DICT for further usage. (see functions)')
        six = (f'[SYSTEM] copyright material from Adel Al-Aali [SYSTEM]')

        print(f"{one:^70}")
        print(f"{two:^70}")
        print(f"{three:^70}")
        print(f"{four:^70}")
        print(f"{five:^70}")
        print(f"{six:^70}")
        print(f"{x * 20: ^70}")
        print(), print()
    @staticmethod
    def period_wait():
        period = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        # multi = [2,2,2,2,2,2,2,2,2,2]
        period_len = len(period)
        with self.Spinner():
            for z, x in enumerate(period):
                print(x)
                time.sleep(.2)
                if z <= period_len:
                    z += 1
                    print(f"{yellow}{x * z}{reset}")
                    continue
                elif z == period_len:
                    break

    @staticmethod
    def clear():
        # check and make call for specific operating system
        os_name = platform.system()
        _ = call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')


class install_dependant():
    def __init__(self):
        def install(self):
            try:
                sucessfull_install = []
                subprocess.check_call([sys.executable, "-m", "pip", "install", threading])
                if subprocess.check_call:
                    print(f'{yellow} Sucessfully Installed PIP')
                    sucessfull_install.append('pip')
                subprocess.check_call([sys.executable, "-m", "tqdm", "install", tqdm])
                if subprocess.check_call:
                    print(f'{yellow} Sucessfully Installed TQDM')
                    sucessfull_install.append('TQDM')
                subprocess.check_call([sys.executable, "-m", "pip", "datetime", datetime])
                if subprocess.check_call:
                    print(f'{yellow} Sucessfully Installed datetime')
                    sucessfull_install.append('datetime')
                subprocess.check_call([sys.executable, "-m", "pip", "net-tools", net - tools])
                if subprocess.check_call:
                    print(f'{yellow} Sucessfully Installed datetime')
                    sucessfull_install.append('net-tools')
                subprocess.check_call([sys.executable, "-m", "apt install", "airmon-ng", airmon - ng])
                if subprocess.check_call:
                    print(f'{yellow} Sucessfully Installed airmon-ng')
                    sucessfull_install.append('airmong-ng')
                print(f'{yellow}**Installed Dependencies {reset}\n{sucessfull_install}')

            except subprocess.CalledProcessError as sub0:
                traceback.print_exc()
                print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub0)}')
            except subprocess.TimeoutExpired as sub1:
                traceback.print_exc()
                print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub1)}')
            except subprocess.SubprocessError as sub2:
                traceback.print_exc()
                print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub2)}')





class BestBuy_ripper(webdriver.Chrome):
    # cart_wait = WebDriverWait
    global timer
    timer = random.randrange(5.0, 8.0)
    global OS
    OS = os.name
    print(OS, 111111)
    # driver = webdriver.Chrome(options=chrome_options, executable_path= r'/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent/chromedriver')
    executable_path = r"/Users/a-robot/Documents/CS/PROJECT/GPU_JACKER/"
    os.environ['PATH'] += executable_path

    chrome_options = Options

    def __init__(self, executable_path=r"/Users/a-robot/Documents/CS/PROJECT/GPU_JACKER/", teardown=False):
        super(BestBuy_ripper, self).__init__()
        self.os.environ['PATH'] += executable_path

        # driver = webdriver.Chrome(options=chrome_options, executable_path= r'/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent/chromedriver')
        self.implicitly_wait(20)
        self.executable_path = executable_path
        self.os.environ['PATH'] += self.executable_path
        self.implicitly_wait(15)
        self.maximize_window()
        self.By = By
        self.Keys = Keys
        self.WebDriverWait = WebDriverWait
        self.Options = Options


    @staticmethod
    def program_dependancies():
        print('Will Add Dependencies Later')
        #### pip install webdriver-manager
        pass

    def install_plugins(self):
        print('Will install plugins later Later')

        pass



    def login(self):

        chrome_options = Options()
        chrome_options.add_extension(
            "/Users/a-robot/Documents/CS/PROJECT/GPU_JACKER/ad_blocker.crx")
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




