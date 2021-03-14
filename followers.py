import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


user=str(input("Ingrese usuario: "))
contra=str(input("Ingrese contra: "))
inp=input("Ingresa los users aqui (separados por coma): ").replace("@","").replace(" ","")

#Puedes cambiar webdriver.Edge por webdriver.Chrome o webdriver.Opera según tu preferencia
browser = webdriver.Edge(r"C:\Users\USER\Downloads\edgedriver_win64\msedgedriver.exe") #Inserta aquí el path de donde está tu webdriver, sustituye solo lo que está dentro de las comillas

browser.get('https://www.instagram.com/accounts/login/?hl=es')
sleep(2)
elem = browser.find_element_by_name("username").send_keys(user)
elem = browser.find_element_by_name("password").send_keys(contra)

good_elem = browser.find_element_by_xpath('//html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button').click()
sleep(2)
browser.get("https://www.instagram.com")
lista=inp.split(",")
for nombre in lista:
    browser.get("https://www.instagram.com/"+nombre+"/") 
    follow = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()




