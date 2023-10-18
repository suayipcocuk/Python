from selenium import webdriver
from time import sleep
import pyautogui


dosya = open("B:\\Yeni klasör\\Çalışmalarım\\Selenium_kullanımı\\hesaplar.txt","r+",encoding="utf-8")

print("Yapmak istediğiniz işlemi seçiniz:","\n","1)Hesapla profil fotoğrafı ekleyin","\n","2)Hesaplara gönderi ekleyin","\n",
"3)Hesapların bir profili takip etmesini sağlayın","\n","4)Bir hesaba (şikayet) spam saldırısında bulunun (AYKIRIDIR!!)","\n",
"5)Hesapların güvensize düşmesini önleyin","\n","6)Özel hesap(Hızlı Login)")

yanıt = int(input("Yanıtınız:"))
miktar = int(input("Üzerinde işlem yapmak istediğiniz hesap miktarı:"))

def h_g_ekle():
    a = 0
    while a != miktar:
        inst = webdriver.Edge("B:\\Yeni klasör\\Çalışmalarım\\Selenium_kullanımı\\msedgedriver.exe")
        inst.set_window_size(300,800)
        inst.get("https://www.instagram.com/accounts/login")
    
        sleep(1)
    
        kllnc_adı = dosya.readline()
    
        email = inst.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
        email.send_keys(kllnc_adı)
    
        h_sifre = dosya.readline()
    
        sleep(0.5)
    
        sifre = inst.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")  
        sifre.send_keys(h_sifre)
        
        sleep(0.5)

        giris_yap = inst.find_element_by_css_selector("#loginForm > div > div:nth-child(3)")
        giris_yap.click()
           
        
        sleep(5)
        
        inst.get("https://www.instagram.com/accounts/task_kllscd/")
        
        for i in range(6):
            sleep(0.3)
            pyautogui.press("tab")
        pyautogui.press("enter")
        
        sleep(2)
        
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
        
        sleep(2)
        
        for i in range(9):
            sleep(0.7)
            pyautogui.press("tab")

        sleep(0.6)
        
        for i in range(a):
            pyautogui.press("right")
        
        if a==0:
            pyautogui.press("right")
            pyautogui.press("left")                 
            pyautogui.press("enter")
        else:
            pyautogui.press("enter")
            
        sleep(5)




                                                    
        for i in range(3):
            sleep(0.4)
            pyautogui.press("tab")
            sleep(0.1)
            pyautogui.press("tab")
            sleep(0.1)
            pyautogui.press("tab")
            sleep(0.1)
            pyautogui.press("enter")
            sleep(0.4)        
        
        
        sleep(30)
        
        inst.close()
    
        a = a+1
    
        if a == miktar:
            print("İşleminiz tamamlandı")
        else:
            print("İşleminiz sürüyor")


def giriss():
    a = 0
    
    inst = webdriver.Edge("B:\\Yeni klasör\\Çalışmalarım\\Selenium_kullanımı\\msedgedriver.exe")
    inst.set_window_size(300,800)
    inst.get("https://www.instagram.com/accounts/login")
    
    sleep(1)
    
    kllnc_adı = input("Kullanıcı Adınız:")
    
    email = inst.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
    email.send_keys(kllnc_adı)
    
    h_sifre =  input("Şifreniz?:")
        
    sleep(0.5)
    
    sifre = inst.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")  
    sifre.send_keys(h_sifre)
        
    sleep(0.5)

    giris_yap = inst.find_element_by_css_selector("#loginForm > div > div:nth-child(3)")
    giris_yap.click()
        
    sleep(4)
    
    inst.close()
    
    a = a+1
    
    if a==1:
        print("İşleminiz tamamlandı")
            
def pp_ekle():
    a = 0
    while a != miktar:
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

        giris_yap = inst.find_element_by_css_selector("#loginForm > div > div:nth-child(3)")
        giris_yap.click()
           
        
        sleep(5)
        
        inst.get("https://www.instagram.com/accounts/edit/")
        
        pp_deis = inst.find_element_by_css_selector("#react-root > section > main > div > article > div > div.XX1Wc > button")
        pp_deis.click
        
        sleep(2)
        
        for i in range(9):
            pyautogui.press("tab")
        
        for i in range(a):
            pyautogui.press("right")
        
        pyautogui.press("enter")
        
        sleep(15)
    
        inst.close()
    
        a = a+1
    
        if a==miktar:
            print("İşleminiz tamamlandı")
        else:
            print("İşleminiz sürüyor")

if yanıt == 6:
    giriss()
elif yanıt == 1:
    miktar = int(input("Üzerinde işlem yapmak istediğiniz hesap miktarı ?:"))
    pp_ekle()
elif yanıt == 2:
    miktar = int(input("Üzerinde işlem yapmak istediğiniz hesap miktarı ?:"))
    h_g_ekle()
elif yanıt == 3:
    miktar = int(input("Üzerinde işlem yapmak istediğiniz hesap miktarı ?:"))
elif yanıt == 4:
    miktar = int(input("Üzerinde işlem yapmak istediğiniz hesap miktarı ?:"))
elif yanıt == 5:
    miktar = int(input("Üzerinde işlem yapmak istediğiniz hesap miktarı ?:"))
else:
    print("ARKADAŞIM DÜZGÜN BİR YANIT GİRERMİSİN ARTIK")
    
