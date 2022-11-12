# DEĞİŞKENLER

# -----------------------------------------------

#Atama deyimi (=)

degisken = 10
z = 5
p = 3
a = "mor"
x = 256.20


# -----------------------------------------------

#  Değişken özellikleri
#– Rakamla başlamaz.
#– Boşluk kullanılmaz.
#– Alt çizgi dışında işaret kullanılmaz.
#– Saklanmış (reserved) kelimeler kullanılmaz.
#– UTF 8 kodlaması yani Türkçe harfler kullanılabilir. Ancak bazı dış
# kütüphanelerde geçerli olmayabilir.
#– Küçük-büyük harfe duyarlıdır. A ve a iki farklı değişken adıdır.

#Uygun değişkenler

degisken = "IEEE"
deg_isken = "IEEE"
_deg_isken = "IEEE"
degiSKeN = "IEEE"
DEGISKEN = "IEEE"
degisken2 = "IEEE"

#Uygun olmayan değişkenler

#2degiskenn = "IEEE"
#deg/isken = "IEEE"
#deg-isken = "IEEE"
#degis ken = "IEEE"

# Case tipleri

# Camel Case, 1. kelime haric diger kelimeler büyük harf ile başlar
benimDegiskenim = 30
# Pascal Case bütün kelimeler büyük harf ile başlar
BenimDegiskenim = 25
# Snake Case kelimeler alttan çizgi ile ayrılır
benim_degiskenim = 35

# Eş zamanlı değer aktarma

h = j = l = 0

u, z, i = 10, 15, 20

#print(h, j, l)
#print(u, z, i)

#print(h,u)

u, h = h, u

#print(h,u)

del h, j, l, u, z, i


#list

meyveler = ["domates", "salatalık", "patlıcan"]

x, y, z = meyveler

#print(x,y,z)

del x, y, z

#Değişkenleri yazdırma

x = "Yine "  #sonlarda boşluk var.
y = "ring "
z = "sırası var."
#print(x + y + z)

del x, y, z

x, y = 5, 10

del x, y
#print(x+y)

x, y = 5, " python"

# Veri tiplerini gözetir ve boşluk bırakmaz
#print(x + y)

# Veri tipi gözetmez ve boşluk bırakır
# print(x, y)

# -----------------------------------------------

# VERİ TİPLERİ

# Metin tipi: str (string)
# Sayısal tipler: int, float, complex
# Sıra tipleri: list, tuple, range
# Haritalama/Eşleme tipi: dict (dictionary)
# Küme tipleri: set, frozenset
# Boolean tipi: bool (false/true)
# Bynary tipleri: bytes, bytearray
# None tipi: NoneType

#Metin tipi örnekleri
a = "Bu bir metindir"
b = "p!006s8"
c = "5"
d = "*/?"
f = "^32+%%+^+'♥♥'"

# int(integer-tam sayı) sayı tipi örnekleri
a = 10
b = 0
c = 50000000000
d = a * b
e = d + b

#print(type(d))

# float(ondalık sayı) sayı tipi örnekleri
a = 20.5
b = 0.00001
c = 5 / 4
d = a * b
e = 5.0
#print(type(e))
#print(type(e))
# print(type(d))

# complex(karışık) sayı tipi örnekleri

a = 1j
b = 5 + 2j
c = 9 + 5j
#print(type(c))

# list (liste) sıralama tipi

a = ["elma", "muz", "kiraz"]
b = ["5", "2", "3"]
c = [5, 2, 3]
d = ["patates", 9, "3", ""]
e = [5,]
# print(type(e))
# print(a[2])

# tuple sıralama tipi

a = ("matematik", "fizik", "kimya")
b = (1, 2, 3)
c = (5, )
#print(type(c))
#print(a[0])

# range veri tipi

a = range(6)
b = range(1, 10, 2)
# range(başlangıç, durma noktası, artış miktari)
#
#print(a)

# dict(dictionary) sözlük veri tipi

x = {"isim": "abdül", "yas": 19}
#print(x["isim"])

# set (küme) veri tipi

a = {"elma", "muz", "kiraz"}
b = {}  #boş küme

# frozen set ise değiştirelemez set'dir

x = frozenset({"elma", "muz", "kiraz"})

# Boolean veri tipi = doğru/yanlış

a = True
b = False

#print(type(a))

# None veri tipi

a = None
#print(a)
#print(type(a))

# Elimizle veri tipini belirtme

# metin için
str()

a = " domates"
b = 5

#print(str(b)+a)

# unsupported operand type(s) for +: 'int' and 'str'

# print(str(b)+a)

str("s1")  # bir şey değişmez
str(2)  # "2" olur
str(3.0)  # "3.0" olur

#sayısal değerler için
int()

int(2.8)  #2'ye yuvarlanır
int(2.1)  #2'ye yuvarlanır
int("2")  #2 olur

float()

float(1)  # 1.0 olur
float(2.8)  # bir şey değişmez
float("3")  # 3.0'e dönüşür
float("4.2")  # 4.2'e dönüşür

complex()

#sıra tipleri için
list()
tuple()

#ve böyle devam eder..

# -----------------------------------------------

#PRINT FONKSIYONU

#print("merhaba")
#print('merhaba')
# arasında hiçbir fark yoktur

# yazım işlemini değişkenler kullanarak daha rahat bir şekilde yapabiliriz
a = "Yemekhanede yine uzun bir sıra var."
# print(a)

# birçok satırdan oluşan bir şey yazdırmak istiyorsanız 3 adet quote kullanabilirsiniz
# 3 adet single quotelar da aynı işlevi görür ('')

a = """Yemekhanede yine önüme birileri geçti, gideyim
de instagram sayfalarına şikayet edeyim
belki bir şeyler düzelir."""

a = """Yemekhanede yine önüme birileri geçti, gideyim
de instagram sayfalarına şikayet edeyim
belki bir şeyler düzelir."""

a = '''Yemekhanede yine önüme birileri geçti, gideyim
de instagram sayfalarına şikayet edeyim
belki bir şeyler düzelir.'''

# Metinler birer dizidir
# 0 veya daha fazla karakterlerden(elemanlardan) oluşan dizilerdir

#print(a[0])
#print(a[23:30])

#Metin uzunluğu len() fonskiyonu ile ölçülebilir

#print(len(a))

# a metini 112 elemandan oluşuyormuş.

#Metinleri parçalara ayırmak

#baştan başlayarak
# a[5] ilk 5 elemanı temsil ediyor
#print(a[:5])

#belli bir noktadan itibaren başlamak istersek
#print(a[5:])

#sondan kesit almak
# print(a[-8:])

#Metinler toplanabilir

b = "yemek"
c = "hane"

y = b + c
# print(y)

# -----------------------------------------------

# Escape karakterleri

# Backslash özel komutları geçersiz asyabilir (\)

#trxt = "Bu yemekte "domates" en önemli malzemedir."
text = "Bu yemekte \"domates\" en önemli malzemedir."
#print(text)

#Fakat o zaman stringe "\" koymak istediğinizde ne yapacaksınız?
# "\\" koyarak kendisini geçersiz kılabilirisiniz

#text = "C:\users\user"
text = "C:\\users\\user"
#print(text)

# Yeni satıra geçmek (\n) (newline)

#print("domates iyidir")

#print("Bunlar\nbirer\nyeni\nsatır")

# Tab (boşluk) (\t) vs.

# -----------------------------------------------

# ARITMETIK OPERATÖRLER
#
#
# + Toplama

x = 5 + 5

# - Çıkarma

x = 10 - 5

# * Çarpma

x = 5 * 10

# / Bölme

x = 100 / 5

# % Mod alma

x = 20 % 3
#print(x)

# ** Üs alma

x = 5**2
#print(x)

# // kalansız bölme (floor division)

x = 20 // 3
#print(x)

# Atama Operatorleri
# Başta ='i görmüştük

x += 3  # X'in değerine 3 ekler
x -= 3  # X'in değerine -3 ekler
x *= 3  # X'in değerini 3'e katlar
x /= 3  # X'in değerini 3'e böler
x %= 3  # X'in değerini mod 3üne eşitler
x //= 3  # X'i 3e bölüp X'in değerini bölüm'e eşitler
x **= 3  # X'in değerini X üssü 3'e eşitler

# Bunlar alttakilerle aynı şeydir

x = x + 3
x = x - 3
x = x * 3
x = x / 3
x = x % 3
x = x // 3
x = x**3

# Booleans, bools
# Yanlış veya Doğru ifadeleri belirtir

a = 200 < 50

# a bu durumda yanlış olur ve False karşılığını alır

# print(a)

# Bazı değerler hariç çoğu değerin boolean değeri True'dur örneğin

#print(bool("Merhaba"))
#print(bool(30))

# bool(False) False
# bool(None) NoneType
# bool(0) Sıfır
# bool("") Boş Metin
# bool(()) Boş Liste
# bool([]) Boş Demet
# bool({}) Boş Küme

# -----------------------------------------------

# Karşılaştırma Operatörleri

# (==) Eşitliği kontrol eder

5 == 10


# Eşit olmadığından False dönecektir.

# (!=) Eşit olmamayı kontrol eder

5 != 10

# Eşit olmadığından True dönecektir.

# (>) büyük olma durumunu kontrol eder

5 > 10

# Büyük olmadığından False dönecektir.

# (<) Küçük olma durumunu kontrol eder

5 < 10

# Küçük olduğundan True dönecektir.
# (<=) küçük eşit olma durumunu kontrol eder
# (>=) büyük eşit olma durumunu kontrol eder

# -----------------------------------------------

# Format Komutu

a = "patates"

#print("Senin adın {}".format(a))

b = 32

#print("Senin adın {}, yaşın ise {}".format(b, a))
# print("Senin adın {1}, yaşın ise {0}".format(a, b))

# -----------------------------------------------

# Input Komutu
#
#a = input("Bana cevap ver.")
#print("verdiğin cevap: " + a)
#kullanıcıdan bir cevap alır ve değişkene atar
#aldığı cevap string olarak hafızaya kaydedilir.

a = float(input("İlk kenarı giriniz:"))
b = float(input("Diğer kenarı giriniz:"))

c = (a**2 + b**2)**0.5

print(c)



