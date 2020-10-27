# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


# Inputs
user =  str(input('Insira o nome do usuário: '))


# Starting webdriver
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/" + user)


# Closing popup
driver.implicitly_wait(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div/div/button').click()


# Downloading photos
photos = driver.find_elements_by_class_name("_9AhH0")
if len(photos) > 0:
    os.mkdir(user)
    countphotos = 0
    countscroll = 0
    while countphotos < len(photos):
        photos[countphotos].screenshot('./{}/img{}.png'.format(user, countphotos))
        driver.execute_script("window.scrollTo({}, {});".format(countscroll, countscroll + 100))
        print('Baixando fotos: {}'.format(countphotos))
        countphotos += 1
        countscroll += 100
        time.sleep(1)
    print('{} fotos baixadas'.format(len(photos)))
else:
    print('A conta não possui fotos disponiveis')
driver.close()
