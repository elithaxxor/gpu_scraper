from gpustealer import BestBuy_ripper
#.add-to-cart-button

with BestBuy_ripper() as rip:
    # rip.install_plugins()
    rip.install_plugins()
    rip.login()
    rip.login_info()
    rip.first_page()

    flag = rip.iterate()

    print(flag)
    counter = 0
    while flag != 'True':
        print(f'Waiting.. [{counter + 2} Seconds]')
        print(f'This many recursions have been processed [{counter}]')
        flag = rip.iterate()
        counter += 2
        continue
    else:
        rip.send_email()
        rip.card_and_order()



    #rip.click_thru_page()

    print('Exiting..')

