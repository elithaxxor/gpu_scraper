import time, datetime
from gpustealer import BestBuy_ripper, Prettify, install_dependants
from datetime import datetime

try:
    print(f'**[STARTING GPU SEQUENCE]**')
    current_time = datetime.now()
    print(current_time)
    with Prettify() as pretty:
        header = pretty.display_header()
        print(header)

except Exception as e:
    print(f'[ERROR IN PARSING HEADER] \n{str(e)}')
    time.sleep(1)


print(), print()
print('X' * 50)
print('X' * 50)
print(), print()


with install_dependants() as install:
    try:
        #install = install_dependants()
        print(f'**[INITIATING DEPENDENCY INSTALL]**')
        plugins = install.install_plugins()
        plugins()
        #install.install_plugins()
        if install.install_plugins():
            print(F'Dependencies Installed: , \n {str(install)} \n {str(plugins)}')
            time.sleep(3)
            print('Installling Dependencies')
            print(install)
        else:
            print(f'[ERROR IN PARSING HEADER] \n')
            pass
    except Exception as E:
        print(f'[ERROR IN PARSING HEADER] \n{str(E)}')
        time.sleep(1)


with BestBuy_ripper() as rip:
    rip.install_plugin()
    rip.login_info()
    rip.first_page()
    flag = rip.iterate()
    print(flag)
    counter = 0
    while flag != 'True':
        if flag == True:
            print('[FOUND A GPU]\n ..Breaking sequence.')
            rip.send_email()
            rip.card_and_order()
            break
        print(f'Waiting.. [{counter + 2} Seconds]')
        print(f'This many recursions have been processed [{counter}]')
        flag = rip.iterate()
        counter += 2
        continue

    else:
        rip.send_email()
        rip.card_and_order()

    rip.send_email()
    rip.card_and_order()
    print('[Exiting..]')





## chormium test
# try:
#     s = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=s)
#
#    # driver = webdriver.Chrome(r"/Users/a-robot/Documents/CS/PROJECT/GPU_JACKER/")  # Optional argument, if not specified will search path.
#     driver.get('http://www.google.com/');
#     time.sleep(5)  # Let the user actually see something!
#     search_box = driver.find_element_by_name('q')
#     search_box.send_keys('ChromeDriver')
#     search_box.submit()
#     time.sleep(5)  # Let the user actually see something!
#     driver.quit()
# except Exception:
#     print('Error in chromedriver loading ')



