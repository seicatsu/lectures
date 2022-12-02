# 10 tane öğesi olan bir liste oluşturun. Her öğenin değeri kendi
# indisinin karesi olsun.
list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# oluşturduğunuz listeden 2'ye tam bölünmeyen öğeleri çıkarın
list2 = []

for i in list:
   if i % 2 == 0:
     list2 = list2 + [i]

print(list2)

#Ekrandan önce bir n tamsayısı okuyun. Sonra, n tane isim okuyun, isimlerden bir liste oluşturun. İsimleri sıralı olarak, her satırda bir isim olacak biçimde ekranda görüntüleyin.

n = int(input("tamsayı giriniz"))
list = []

for i in range(n):
    a = input("isim giriniz")
    list = list + [a]

for i in list:
    print(i)

print(list)

# Kullanıcıdan isteyeceğimiz bir tamsayıya kadar pozitif sayılardan oluşan
#bir liste oluşturun. Oluşan listeden iki tane yeni liste oluşturun.
#Birinci listede tek sayılar, ikinci listede çift sayılar olsun.

n = int(input("tamsayı giriniz"))
list = []

for i in range(1,n):
  list = list + [i]
  
print(list)

listtek = []
listcift = []

for i in list:
  if i % 2 == 0:
    listcift = listcift + [i]
  elif i % 2 != 0: 
    listtek = listtek + [i]

print(listtek)
print(listcift)



---------------------------

# FONKSİYON ÖRNEĞİ

#: Bir listeyi parametre olarak alan ve tekrarlanan öğeleri listeden çıkartıp yeni bir liste oluşturan bir fonksiyon yazınız. Fonksiyon oluşturduğu listeyi çağırıldığı yere döndürsün. Örneğin:
# liste [4,5,4,4,6,5] ise yeni liste: [4,5,6] olsun.

liste = [4,5,4,4,6,5]
liste2 = [5,6,7,5,5,3,3,2]

def fonk(a):
  for i in a:
     if a.count(i)>1:
        a.remove(i)
  a.sort()
  return a

x = fonk(liste)
print(x)

b = fonk(liste2)
print(b)
