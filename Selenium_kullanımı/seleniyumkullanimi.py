from selenium import webdriver
from time import sleep

inst = webdriver.Edge("B:\\Yeni klasör\\Çalışmalarım\\Selenium_kullanımı\\msedgedriver.exe")
dosya = open("B:\\Yeni klasör\\Çalışmalarım\\Selenium_kullanımı\\hesaplar.txt","r+",encoding="utf-8")

a=0

while True:
    inst.get("https://www.instagram.com/accounts/login/")

    sleep(4)
    
    kllnc_adı = dosya.readline()
    
    email = inst.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
    email.send_keys("task_kllscd")

    sleep(1)
    
    h_sifre = dosya.readline()
    
    sleep(1)
    
    sifre = inst.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")
    sifre.send_keys("yaaselya46")

    sleep(2)

    giris_yap = inst.find_element_by_css_selector("#loginForm > div > div:nth-child(3)")
    giris_yap.click()

    sleep(15)
    
    gonderi_ekl = inst.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button ")
    sleep(1)
    gonderi_ekl.click
    
    
    degıl = inst.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button")
    degıl.click()

    sleep(1)

    degıll = inst.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
    degıll.click()

    sleep(10)
    
    inst.close()

    if a==3:
        break
    
    else:
        print("işlem sürüyor")

if a==3:
        print("işlem bitti")

