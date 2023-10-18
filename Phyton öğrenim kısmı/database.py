import sqlite3

con = sqlite3.connect("Pandemik.db")
cursor = con.cursor()


def pandemik():
    cursor.execute("CREATE TABLE IF NOT EXISTS Öğrenciler (ad TEXT,Yaş INT,Aşı_sayısı INT,Kalan_Aşı INT)")
    con.commit 
    con.close()  

def veri_ekle():
    cursor.execute("İNSERT İNTO Öğrenciler (ism-soyism,yas,ası,Kalan_ası) VALUES (?,?,?,?)",(ism_soyism,yas,ası,kalan_ası))
    con.commit
    con.close()

pandemik()
veri_ekle()

print("Pandemi kapsamında aşı veri toplama Yazılımı")

ism_soyism=input("İsim-Soyisim:")
yas=input("Yaşınızı girin: ")
ası = int(input("Lütfen pandemi kapsamında olduğunuz aşı sayısını giriniz (Hiç aşı olmamışsanız 0 yazınız):"))

kalan_ası = (ası - 3)

if ası<3:
    print("Aşınız eksik:")

elif ası<4 and -1>ası :
    print("Doğrulandı")
elif ası > 4 and -1<ası :
    print("Lütfen geçerli aşı sayınızı girin")   
else:
    print("Aşı sayınız '3' İlginizden dolayı teşekkür ederiz,sağlıklı günler dileriz.")
if ası==1:
    print("Olmanız gerekken aşı sayısı 2'dir.")
    print("Lütfen en yakın aşı merkezlerimizden aşılarınızı olunuz.")

if ası==2:
    print("Olmanız gerekken aşı sayısı 1'dir.")
    print("Lütfen en yakın aşı merkezlerimizden aşınızı olunuz.")

if ası==0:
    print("Olmanız gerekken aşı sayısı 3'dür.")
    print("Lütfen en yakın aşı merkezlerimizden aşılarınızı olunuz.")
