
sayi1=int(input("sayi gir"))
sayi2=int(input("sayi gir"))
secim=input("1/toplama2/cikarma 3/carp4/bol")
if secim=="1":
    sonuc=sayi1+sayi1
    print("sonuc budur",sonuc)
elif secim=="2":
    if sayi1>sayi2:
        sonuc=sayi1-sayi2
        print("sonucu",sonuc)
    else:
        sonuc=sayi2-sayi1
        print("sonuc",sonuc)
elif secim=="3":
    sonuc=sayi1+sayi2
    print("sonnucu",sonuc)
elif secim=="4":
    if sayi1>sayi2:
        sonuc=sayi1%sayi2
        print("sonnucu",sonuc)
    else:
        sonuc=sayi2/sayi1
        print("sonucu",sonuc)
else:
    exit(0)
