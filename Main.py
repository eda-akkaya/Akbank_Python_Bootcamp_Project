# PyCharm Community Edition 2022.3.3
# Akbank Python Bootcamp Projesi
# Eda Akkaya  5. grup

import csv
import datetime

class PizzaSinifi():                      # Base pizza class
    def __init__(self,ad,tanim,fiyat):    # Constructor
        self.tanim = tanim
        self.fiyat = fiyat
        self.ad = ad

    def get_description(self):
        return self.tanim

    def get_cost(self):
        return self.fiyat

    def get_name(self):
        return self.ad

# pizza subclasses
class KlasikPizzaSinifi(PizzaSinifi):
    klasikPizza = PizzaSinifi(ad = "Klasik Pizza", tanim="Özel pizza sosu, pizza peyniri, sucuk, salam, sosis, yeşil biber",fiyat=75)

class MargheritaPizzaSinifi(PizzaSinifi):
    margheritaPizza = PizzaSinifi(ad = "Margherita Pizza", tanim= "Mozzarella peyniri, küp domates, roka, özel domates sosu",fiyat=85)

class TurkPizzaSinifi(PizzaSinifi):
    turkPizza = PizzaSinifi(ad = "Turk Pizza" ,tanim="Özel sos, kavurma, yeşil biber, kırmızı biber",fiyat=100)

class DominosPizzaSinifi(PizzaSinifi):
    dominosPizza = PizzaSinifi(ad = "Dominos Pizza", tanim= "Domates sos, mozzarella peyniri,  sucuk, kekik",fiyat=120)

class SadePizzaSinifi(PizzaSinifi):
    sadePizza = PizzaSinifi(ad = "Sade Pizza", tanim="Domates sos, sucuk, mozzarella peyniri", fiyat= 65)


class DecoratorSinifi():               # Base decorator class
    def __init__(self,tanim,fiyat):    # Constructor
        self.tanim = tanim
        self.fiyat = fiyat

    def get_description(self):
        return self.tanim
    def get_cost(self):
        return self.fiyat

# decorator subclasses
class ZeytinDecoratorSinifi(DecoratorSinifi):
    zeytinSos = DecoratorSinifi(tanim="zeytin", fiyat= 5 )

class MantarDecoratorSinifi(DecoratorSinifi):
    mantarSos = DecoratorSinifi(tanim="Mantar",fiyat=20)

class KeciPeyniriSinifi(DecoratorSinifi):
    keciPeyniriSos = DecoratorSinifi(tanim="Keçi peyniri", fiyat=40)

class EtSinifi(DecoratorSinifi):
    etSos = DecoratorSinifi(tanim="Et", fiyat=80)

class SoganSinifi(DecoratorSinifi):
    soganSos = DecoratorSinifi(tanim="Soğan",fiyat= 7 )

class MisirSinifi(DecoratorSinifi):
    misirSos = DecoratorSinifi(tanim="Mısır", fiyat= 12)

def pizza_adi_döndür(secim):      # Girilen no'ya göre pizzanın türünü döndüren fonksiyon
    pizza_adi = ''
    if secim == 1:
        pizza_adi = "Klasik Pizza"
    elif secim == 2:
        pizza_adi =  "Margherita Pizza"
    elif secim == 3:
        pizza_adi = "Turk Pizza"
    elif secim == 4:
        pizza_adi = "Sade Pizza"
    return pizza_adi

def sos_adi_döndür(secim):    # Girilen no'ya göre sosun türünü döndüren fonksiyon
    sos_adi = ''
    if secim == 11:
        sos_adi = "Zeytin"
    elif secim == 12:
        sos_adi =  "Mantar"
    elif secim == 13:
        sos_adi = "Keci Peyniri"
    elif secim == 14:
        sos_adi = "Et"
    elif secim == 15:
        sos_adi = "Sogan"
    elif secim == 16:
        sos_adi = "Misir"
    return sos_adi

def pizza_numara_gir(secim):      # Girilen pizza no'suna göre sipariş detayını döndüren fonksiyon
    pizza_secimi =''
    if secim == 1:
        pizza_secimi = KlasikPizzaSinifi.klasikPizza
    elif secim == 2:
        pizza_secimi = MargheritaPizzaSinifi.margheritaPizza
    elif secim == 3:
        pizza_secimi = TurkPizzaSinifi.turkPizza
    elif secim == 4:
        pizza_secimi = SadePizzaSinifi.sadePizza
    else:
        print( "Yanlış giriş yaptınız !")

    print ("Pizza türü: " + pizza_adi_döndür(pizza_secim_no) +"\nPizza içeriği: " + pizza_secimi.get_description() +"\nTutar: " + str(pizza_secimi.get_cost()) + " TL")
    return pizza_secimi.get_cost()


def sos_no_gir(secim):   # Girilen sos no'suna göre sipariş detayını döndüren fonksiyon
    sos_secimi = ''

    if secim == 11:
        sos_secimi = ZeytinDecoratorSinifi.zeytinSos
    elif secim == 12:
        sos_secimi = MantarDecoratorSinifi.mantarSos
    elif secim == 13:
        sos_secimi = KeciPeyniriSinifi.keciPeyniriSos
    elif secim == 14:
        sos_secimi = EtSinifi.etSos
    elif secim == 15:
        sos_secimi = SoganSinifi.soganSos
    elif secim == 16:
        sos_secimi =MisirSinifi.misirSos
    else:
        print( "Yanlış giriş yaptınız !")
    print  ("Sos: " + sos_secimi.get_description() + "\nTutar: " + str(sos_secimi.get_cost()) + " TL")
    return sos_secimi.get_cost()

 #  main fonksiyonu
if __name__ == '__main__':
    yeni_musteri_var_mi = True
    musteri_listesi = []

    while yeni_musteri_var_mi:          # Tabloya istenildiği takdirde müşteri eklenebilsin diye kurulan while döngüsünün başlangıcı
        #Bu fonksiyon önce menüyü ekrana yazdıracaktır.
        menu = open("Menu.txt")
        print(menu.read())

    # Ardından kullanıcının menüden bir pizza ve sos seçmesine imkan tanıyacaktır.
        pizza_secim_no = int(input("Pizza için sayı (1-4) giriniz: "))

        # Seçim için uygun sayının girilip girilmediği kontrol ediliyor
        if (pizza_secim_no <= 0) and (pizza_secim_no > 4):
            pizza_secim_no = int(input("Lütfen pizza için geçerli bir sayı giriniz: "))
        pizza_numara_gir(pizza_secim_no)
        print("--- --- --- --- --- --- ---")
        sos_secim_no = int(input("Sos için sayı(11-16) giriniz: "))
        if (sos_secim_no > 16) and (sos_secim_no < 11) :
            sos_secim_no = input("Lütfen sos için geçerli bir sayı giriniz: ")
        sos_no_gir(sos_secim_no)

        print("\n\n")
        print(" ________________")
        print("| SIPARIS OZETI  |")
        print("|________________|")

        pizza_bilgi_ve_tutar = pizza_numara_gir(pizza_secim_no)
        sos_bilgi_ve_tutar = sos_no_gir(sos_secim_no)
        toplam_tutar = str(pizza_bilgi_ve_tutar + sos_bilgi_ve_tutar)  # Seçilen ürünlerin toplam fiyatını hesaplanıyor
        print("-------------------------------------------------------Toplam tutar: " + toplam_tutar + " TL" )

        islem_anı = datetime.datetime.now()
        siparis_zamani = datetime.datetime.ctime(islem_anı)

    # Seçilen ürünlerin toplam fiyatını hesapladıktan sonra kullanıcıdan isim,
    # TC kimlik numarası, kredi kartı numarası ve kredi kartı şifresi istenmektedir.
        kullanici_adi = input("Adınızı giriniz: ")
        tc_no = input("TCnizi giriniz: ")
        kredi_karti_no = input("Kredi kartı numaranızı giriniz: ")
        kredi_karti_sifre = input("Şifrenizi giriniz: ")
        musteri_bilgi = kullanici_adi, tc_no, kredi_karti_no, pizza_adi_döndür(pizza_secim_no), sos_adi_döndür(sos_secim_no),toplam_tutar, siparis_zamani, kredi_karti_sifre
        musteri_listesi.append(musteri_bilgi)   # her müşteriye ait bilgiler listeye ekleniyor

        cevap = input("Musteri eklemek istiyor musunuz? (E/e|H/h)")    # while döngüsünün devamı için müşteri eklenip eklenmeyeceği soruluyor.

        if cevap =="e":
            yeni_musteri_var_mi = True
        else :
            yeni_musteri_var_mi = False
    # while döngüsünün sonu

#Veritabanı olarak adlandırdığımız "Orders_Database.csv" dosyasında pizzasını seçen
# ve kullanıcı adını, kullanıcı kimliğini, kredi kartı bilgilerini, sipariş açıklamasını,
# sipariş zamanını ve kredi kartı şifresini tutan bir tablo oluşturuluyor.

with open('Orders_Database.csv', mode='w') as musteri_tablosu:
    yazici = csv.writer(musteri_tablosu)
    yazici.writerows(musteri_listesi)
    musteri_tablosu.close()



with open('Orders_Database.csv',mode="r") as musteri_tablosu:
    okuyucu = csv.reader(musteri_tablosu)
    for row in okuyucu:
        if row != [ ]:
            print(row)

# kod sonu