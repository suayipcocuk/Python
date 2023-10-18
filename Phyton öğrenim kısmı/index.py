import os

os.chdir('E:\\')
dosya=open("Pandemikk.db", "a")

import sqlite3

con = sqlite3.connect("Pandemik.db")
cursor = con.cursor()

print("Pandemi kapsamında aşı veri toplama Yazılımı")
dosya.write("Pandemi kapsamında aşı veri toplama Yazılımı")

ism_soyism=input("İsim-Soyisim:")
yas=input("Yaşınızı girin: ")
ası = int(input("Lütfen pandemi kapsamında olduğunuz aşı sayısını giriniz (Hiç aşı olmamışsanız 0 yazınız):"))

def pandemik():
    cursor.execute("CREATE TABLE IF NOT EXISTS Öğrenciler (ad TEXT,Yaş INT,Aşı sayısı INT,Kalan Aşı INT)")
    con.commit  

pandemik()


dosya.write("\n")
dosya.write("\n*")
dosya.write("İsim Soyisim:")
dosya.write(ism_soyism)
dosya.write("\n*")
dosya.write("Yaşı:")
dosya.write(yas)

if ası<3:
    print("Aşınız eksik:")
    dosya.write("\n*")
    dosya.write("Aşısı eksik")
elif ası<4 and -1>ası :
    print("Doğrulandı")
elif ası > 4 and -1<ası :
    print("Lütfen geçerli aşı sayınızı girin")   
else:
    print("Aşı sayınız '3' İlginizden dolayı teşekkür ederiz,sağlıklı günler dileriz.")
    dosya.write("\n*")
    dosya.write("Aşı tam")
if ası==1:
    print("Olmanız gerekken aşı sayısı 2'dir.")
    print("Lütfen en yakın aşı merkezlerimizden aşılarınızı olunuz.")
    dosya.write("\n*")
    dosya.write("Kalan aşı sayısı 2")

if ası==2:
    print("Olmanız gerekken aşı sayısı 1'dir.")
    print("Lütfen en yakın aşı merkezlerimizden aşınızı olunuz.")
    dosya.write("\n*")
    dosya.write("Kalan aşı sayısı 1")
if ası==0:
    print("Olmanız gerekken aşı sayısı 3'dür.")
    print("Lütfen en yakın aşı merkezlerimizden aşılarınızı olunuz.")
    dosya.write("\n*")
    dosya.write("Olması gereken aşı sayısı 3")

dosya.close()   