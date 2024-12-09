# This is a sample Python script.
from myfirstproject import name


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
aralik = range(12)
print(*aralik)
print(*range(2, 20, 5))
aralik2 = range(4, 20, 3)
print(list(aralik2))
print(set(aralik))
#%% tuple veri tipi
#immutable(değiştirilemez)
#read-only(sadece okunabilir)
#Elemanların sequnce numberları vardır(elemanların sıralama numaraları)
#tuple()  ()
tup1 = (2, "quen", 3 + 2j, 2, 34, 5, 7, 2)
print(tup1[2])
print(tup1[::1])
print(tup1[-1:0:-1])
print(tup1.count(2))
print(tup1.index(34))

liste1 = [2, 4, 6, 7]
tuple2 = (2, 5, 9, 12, 16)
set2 = {3, 67, 23, 0}

print(sum(liste1))
print(sum(tuple2))
print(sum(set2))
print(min(liste1))
print(len(set2))

#liste yapısı
liste = [2, 5, 7, 9, 11, 90]
print(liste[:])
print(len(liste))
print(liste[1:4:2])
#listelerde ekleme,güncelleme ve silme işlemleri
isimler = ['selami', 'cetin', 'kral']
print(isimler)
del isimler[0]
isimler[0] = 'enbirinciyazilimci'
print(isimler)
isimler += 'namik', 'ahmet'
print(isimler)
print(isimler[1:3:2] + isimler[3:])
yaslar = [23, 45, 78]
yeniliste = yaslar + isimler
yeniliste.append(24)
yeniliste.insert(3, 'SELAMI')
print(yeniliste)
yeniliste.remove(23)
yeniliste.reverse()
print(yeniliste)
bilgiler = [134,145,'software','Goat']
print(bilgiler)
liste1=[3,4,5,7]
liste2=[9,87,89,90]
liste1+=liste2
print(liste1)

set1={2,5,67,89}
print(set1)
set1.add(45)
set1.remove(5)
set1.clear()
print(set1)
set1={3,56,78,98,20}
print(set1)
set5=set1.copy()
set1.discard(67)
print(set1)
set2={77,87,3}
set3={87,77,50,3,56}
print(set2.intersection(set3))
set1.intersection_update(set2)
print(set1)
print(set3.isdisjoint(set2))
print(set2.isdisjoint(set3))
print(set2.issubset(set3))
print(set3.issuperset(set2))
set1.pop()
print(set1)
print(set2.symmetric_difference(set3))
set2.symmetric_difference_update(set3)
print(set2)
print(set3.union(set2))
set1.update({34,67,89})
print(set1)
#dictionary(sözlük) yapısı
#mutable(değiştirilebilir)
#Elemanların sequence numberı yerine (sira numarası) yerine "KEY" vardır.
#dict()  { }
sozluk={1:"selami",2:"cetin",3:"software engineer"}
print(sozluk[2])
print(sozluk.get(5,"Bu key sozlukte yoktur"))
anahtarlar=[0,1,2,3]
degerler=["ali","veli","ahmet","hacı"]
sozcukdegerleri=zip(anahtarlar,degerler)
#print(sozcukdegerleri)
#print(*sozcukdegerleri)
keys=("ali","veli","eli")
values=['insaat muhendisi',
        'yazilim muhendisi',
        'veteriner']
#ages=[23,21,34]
sozlukelemanlari=zip(keys,values)
bilgiler=dict(sozlukelemanlari)
print(bilgiler)
print(bilgiler["ali"])
sozluk2={1:"ali",1:"veli"}
print(sozluk2[1])

print(bool(0))
set4={2,4,5}
print(set4.pop())