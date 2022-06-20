import time

from pywebio.input import *
from pywebio.output import *

bakiye, tutar = 1000, 0
options = ["Bakiye Gorunteleme", "Para Cekme", "Para Yatirma", "Islem gecmisi", "Cikis"]
islemGecmisi = [["\tTarih", "Yapilan islem", "Bakiye"]]

def main():

    clear()
    islem = radio("Yapmak istediginiz islemi seciniz", options=options)
    if islem == options[0]:
        bakiyeGoruntule()
    elif islem == options[1]:
        paraCek()
    elif islem == options[2]:
        paraYatir()
    elif islem == options[3]:
        islemGecmis()
    elif islem == options[4]:
        cikis()
    else:
        put_error("Lutfen secim yapiniz")
        put_button("Ana sayfa", onclick=lambda: main())


def bakiyeGoruntule():
    clear()
    put_markdown(f"# Bakiyeniz: {bakiye} $")
    put_button("Ana sayfa", onclick=lambda: main())

def paraCek():

    clear()
    global bakiye

    tutar = input("Cekmek istediginiz tutari giriniz: ", type=FLOAT)

    if tutar <= bakiye:
        bakiye -= tutar
        put_markdown(f"# **Islem gerceklestirilmistir...\tKalan bakiyeniz: {bakiye} $**")
        islemGecmisi.append([tarih(), style(put_text(f"-{tutar} $"), 'color:red'), f'{bakiye} $'])
    else:
        put_markdown(" # **Bakiyenizi kontrol ediniz**")

    put_button("Ana sayfa", onclick=lambda: main())

def paraYatir():
    clear()
    global bakiye

    tutar = input("Lütfen yatırmak istediğiniz tutarı girip banknotları bölmeye yerleştiriniz", type=FLOAT)

    bakiye += tutar
    put_markdown(f" # **Yeni bakiyeniz: {bakiye} $**")
    islemGecmisi.append([tarih(), style(put_text(f"+{tutar} $"), 'color:green'), f'{bakiye} $'])

    put_button("Ana sayfa", onclick=lambda: main())

def islemGecmis():
    clear()
    put_table(islemGecmisi)
    put_button("Ana sayfa", onclick=lambda: main())

def cikis():
    clear()
    put_success("Gule gule :)")

def tarih():
    return time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())

if __name__ == '__main__':
    main()
