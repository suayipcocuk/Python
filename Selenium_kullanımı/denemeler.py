from selenium import webdriver
from time import sleep
import pyautogui



dosya = open("B:\\Yeni klasör\\Çalışmalarım\\Selenium_kullanımı\\hesaplar.txt","r+",encoding="utf-8")
miktar = int(input("Üzerinde işlem yapmak istediğiniz hesap miktarı ?:"))

a=0

inst = webdriver.Edge("B:\\Yeni klasör\\Çalışmalarım\\Selenium_kullanımı\\msedgedriver.exe")
inst.get("https://www.instagram.com/accounts/login/")
    
sleep(1)
    
kllnc_adı = dosya.readline()
    
email = inst.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
email.send_keys(kllnc_adı)
    
h_sifre = dosya.readline()
        
sleep(1)
    
sifre = inst.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")  
sifre.send_keys(h_sifre)
    
sleep(0.5)

pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
        
           
        
sleep(5)
        
inst.get("https://www.instagram.com/accounts/edit/")
        
pp_deis = inst.find_element.css_selector("#react-root > section > main > div > article > div > div.XX1Wc > button")
pp_deis.click
