# Örnekler

# IF ÖRNEKLERİ

#Kullanıcıdan bir tane sayı isteyin. Sayının tek mi veya çift mi
#olduğunu söyleyin.

sayi = int(input("sayi giriniz"))

if sayi % 2 == 0:
 print("sayı çifttir")
elif sayi % 2 == 1:
 print("sayı tektir")
else:
 print("hatalı girdi")



#Alışveriş fiyatı girin, İstanbula gidecekse 5 tl, Ankaraya gidecek ise 15 tl
#Kargo ücreti olsun ayrıca kargo ücreti İstanbulda 50 tl üstünde ücretsiz olsun.
#Ankarada ise 100 tl üstüne ücretsiz olsun.

fiyat = int(input("alışveriş tutarı: "))
lokasyon = input("adres: ")

if lokasyon.lower() == "istanbul":
  if fiyat >= 50:
    print("Kargo ücretiniz yoktur.")
  else:
    print("Kargo ücretiniz 5 tl")
if lokasyon.upper() == "ANKARA":
  if fiyat >= 100:
    print("Kargo ücretiniz yoktur.")
  else:
    print("Kargo ücretiniz 15 tl")
    
    
#Harf notu hesaplayalım.

vize = float(input("vize notu: "))
final = float(input("final notu: "))

dönemsonu = 0.40*vize + 0.60*final


if dönemsonu <= 100 and dönemsonu > 95:
     print("A1 ile geçtiniz.")
elif dönemsonu <= 95 and dönemsonu > 90:
     print("A2 ile geçtiniz")
elif dönemsonu <= 90 and dönemsonu > 85:
     print("A3 ile geçtiniz")
elif dönemsonu <= 85 and dönemsonu > 80:
     print("B1 ile geçtiniz")
elif dönemsonu <= 80 and dönemsonu > 75:
     print("B2 ile geçtiniz")
elif dönemsonu <= 75 and dönemsonu > 70:
     print("B3 ile geçtiniz")
elif dönemsonu <= 70 and dönemsonu > 65:
     print("C1 ile geçtiniz")
elif dönemsonu <= 65 and dönemsonu > 60:
     print("C2 ile geçtiniz")
elif dönemsonu <= 60 and dönemsonu > 55:
     print("C3 ile geçtiniz")
elif dönemsonu <= 55 and dönemsonu > 50:
     print("DD ile geçtiniz")
elif dönemsonu < 50:
     print("kaldınız")

#3 tane sayıdan hangisi büyük bunu hesaplayalım.

a = input("a sayisi:")
b = input("b sayisi:")
c = input("c sayisi:")

if a > b and a > c:
  print(f"en büyük sayı {a}")
elif b > a and b > c:
  print(f"en büyük sayı {b}")
else:
  print(f"en büyük sayı {c}")
  
# Girilen bir sayıdan 0'a kadar sayan bir program yazınız.

girdi = int(input("sayi: "))
i = 0
while i < girdi:
  print(girdi)
  girdi = girdi - 1
  
#1'den okunan tamsayıya kadar olan sayıların toplamını hesaplayınız

sayi = int(input("sayi: "))
toplam = 0

while 0 < sayi:
  toplam = toplam + sayi
  sayi = sayi -1

print(toplam)


#Faktöriyel alan program yazalım

sayi = int(input("sayi: "))
faktoriyel = 1

while 0 < sayi:
  faktoriyel = faktoriyel * sayi
  sayi = sayi -1

print(faktoriyel)

#Asal sayı olup olmadığını gösteren program

sayi = int(input("sayi: "))
i = 1
bolensayisi = 0 

while sayi >= i:
  if sayi % i == 0:
    bolensayisi = bolensayisi + 1
  i = i + 1 
  
# FOR ÖRNEKLERİ

# Girilen bir sayıdan 0'a kadar sayan bir program yazınız.

girdi = int(input("girdi: "))

for i in range(girdi):
   print(girdi, end=" ")
   girdi = girdi - 1

if bolensayisi == 2:
  print("asal sayı")
else:
  print("asal degildir")

#1'den okunan tamsayıya kadar olan sayıların toplamını hesaplayınız

girdi = int(input("girdi: "))
toplam = 0

for i in range(girdi):
   toplam = toplam + i

print(toplam)

#Faktöriyel alan program yazalım

girdi = int(input("girdi: "))
faktoriyel = 1

for i in range(1,girdi+1):
    faktoriyel = faktoriyel * i

print(faktoriyel)

#Asal sayı olup olmadığını gösteren program

girdi = int(input("girdi: "))
bolensayisi = 0

for i in range(1,girdi+1):
  if girdi % i == 0:
    bolensayisi = bolensayisi + 1

if bolensayisi == 2:
  print("asal sayidir.")
else:
  print("asal sayi degildir.")
  
#2 kelime isteyin ve 2. kelimede olan harflerin aynılarının 1. kelime içinde yazılmasını isteyin

kelime = input("kelime giriniz")
kelime2 = input("kelime giriniz")

for i in kelime:
   if i in kelime2:
     print(i, end="")
