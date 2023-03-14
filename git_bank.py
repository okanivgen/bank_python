from git_bank_library import bank

# müşteri bilgileri için boş bir liste oluşturuldu
musteri_bilgileri = []

# toplam bakiye başlangıçta 0 olarak atanır
toplam_bakiye = 0


def hesap_bilgi():
    # global anahtar kelimesi kullanılarak değişkenin global olacağı belirtilir
    global musteri_bilgileri
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")
    hesap_no = int(input("Hesap numaranızı giriniz: "))
    kart_sifre = int(input("Kart şifrenizi giriniz: "))
    bakiye = int(input("Bakiyenizi giriniz: "))

    # bank sınıfından bir nesne oluşturulur ve müşteri bilgileri listesine eklenir
    musteri = bank(hesap_no, ad, soyad, kart_sifre)
    musteri.bakiye(bakiye)
    musteri_bilgileri.append(musteri)
    print("Bilgileriniz kaydedildi.\n")


def para_yatir():
    # global anahtar kelimesi kullanılarak değişkenin global olacağı belirtilir
    global toplam_bakiye
    global musteri_bilgileri

    # yatırılacak tutar kullanıcıdan alınır
    yatirilan_tutar = int(input("Yatırılacak tutarı giriniz: "))

    # müşteri_bilgileri listesindeki tüm müşterilerin hesaplarına yatırılacak tutar eklenir
    for musteri in musteri_bilgileri:
        musteri.bakiye(yatirilan_tutar)

    # toplam bakiye hesaplanır
    for musteri in musteri_bilgileri:
        toplam_bakiye += sum(musteri.s5())

    print("Toplam bakiye: ", toplam_bakiye)


def para_cek():
    # global anahtar kelimesi kullanılarak değişkenin global olacağı belirtilir
    global toplam_bakiye
    global musteri_bilgileri

    # tüm müşterilerin hesaplarından çekilecek tutar alınır
    cekilen_tutar = int(input("Çekilecek tutarı giriniz: "))

    # müşteri_bilgileri listesindeki tüm müşterilerin hesaplarından çekilen tutar çıkarılır
    for musteri in musteri_bilgileri:
        musteri.bakiye(-cekilen_tutar)

    # toplam bakiye hesaplanır
    for musteri in musteri_bilgileri:
        toplam_bakiye += musteri.s5()[0]

    print("Yeni güncel bakiye: ", toplam_bakiye)
