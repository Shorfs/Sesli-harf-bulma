sesli_harfler = "aeıioöuü"
sayac = 0

kelime = input("Bir kelime giriniz: ")

def seslidir(harf):
    return harf in sesli_harfler

for harf in kelime:
    if seslidir(harf):
        sayac += 1

mesaj = "{} kelimesinde {} sesli harf var."
print(mesaj.format(kelime, sayac))