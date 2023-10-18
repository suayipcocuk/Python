import sqlite3 as sql

vt = sql.connect("Pandemikk.sqlite")
im = vt.cursor()

print("Pandemi kapsamında aşı veri toplama Yazılımı")

Ad = input("İsim:")
Yaş = input("Yaşınızı girin: ")
Aşı_sayısı = int(input("Lütfen pandemi kapsamında olduğunuz aşı sayısını giriniz (Hiç aşı olmamışsanız 0 yazınız):"))

def pandemik():
    im.execute("CREATE TABLE IF NOT EXISTS Öğrenciler (Ad TEXT,Yaş INT,Aşı_sayısı INT)")
    vt.commit 

def veri_ekle():
    im.execute("INSERT INTO Öğrenciler (Ad,Yaş,Aşı_sayısı) VALUES (?,?,?)",(Ad,Yaş,Aşı_sayısı))
    vt.commit
    vt.close()

if Aşı_sayısı<3:
    print("Aşınız eksik:")

elif Aşı_sayısı<4 and -1>Aşı_sayısı :
    print("Doğrulandı")
elif Aşı_sayısı > 4 and -1<Aşı_sayısı :
    print("Lütfen geçerli aşı sayınızı girin")    
else:
    print("Aşı sayınız '3' İlginizden dolayı teşekkür ederiz,sağlıklı günler dileriz.")
if Aşı_sayısı==1:
    print("Olmanız gerekken aşı sayısı 2'dir.")
    print("Lütfen en yakın aşı merkezlerimizden aşılarınızı olunuz.")

if Aşı_sayısı==2:
    print("Olmanız gerekken aşı sayısı 1'dir.")
    print("Lütfen en yakın aşı merkezlerimizden aşınızı olunuz.")

if Aşı_sayısı==0:
    print("Olmanız gerekken aşı sayısı 3'dür.")
    print("Lütfen en yakın aşı merkezlerimizden aşılarınızı olunuz.")
    
pandemik()
veri_ekle()