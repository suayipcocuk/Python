import sqlite3

vt = sqlite3.connect("vt.sqlite")

im = vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS
    personel (isim, soyisim, sehir, eposta)""")

im.execute("""INSERT INTO personel VALUES
    ("Şuayip", "Çocuk", "KMaraş", "suayipcocuk@gmail.com")""")

vt.commit()
vt.close()