# Örnek 20: Kullanıcıya sinema ya da tiyatro tercihi sorulsun. 
# Sinema izlemek için 15 TL, tiyatro için 10 TL ödenmesi gerekmedir. 
# Öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise 
# indirim yapılan; öğrenci değilse indirimsiz tutarı 
# hesaplayarak ekrana yazdıran kodu yazınız.

secim = int(input("Tiyatro için  1 yazın sinema için 2 yazın ogrenci tiyatro icin 3 ogrenci sinema icin 4"))
kackisi = int(input("kaç kişilik istiyorsunuz"))

if secim == 1:
    fiyat = (kackisi*10)
    print(f"fiyatınız {fiyat} {kackisi} kişisiniz iyi seyirler")

elif secim ==2:
    fiyat = (kackisi*15)
    print(f"fiyatınız {fiyat} {kackisi} kişisiniz iyi seyirler")

elif secim ==3:
    fiyat =(kackisi*5)
    print(f"fiyatınız{fiyat} {kackisi} kişisiniz öğrencilerimizden gurur duyuyoruz iyiki varsınız siz bu ülkenin geleceğisiniz")

elif secim ==4:
    fiyat = float(kackisi*7.5)
    print(f"fiyatınız{fiyat} {kackisi} kişisiniz öğrencilerimizden gurur duyuyoruz iyiki varsınız siz bu ülkenin geleceğisiniz")

else:
    print("yanlış tuş tekrar deneyiniz")
