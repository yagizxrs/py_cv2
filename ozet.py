name = input("Adınızı giriniz: ")
age = input("yaşınızı giriniz: ")
size = float(input("Boyunuzu giriniz: "))

secim = input("Secim yapınız N/A/S/M: \nN: İSİM\nA: YAŞ\nS: BOY\nM: MENÜ")

if secim == "N":
    print("Adınız " + name)
elif secim == "A":
    print("Yaşınız " + age)
elif secim == "S":
    print("Boyunuz: ", size)
elif secim == "M":
    print("Secim yapınız N/A/S/M: \nN: İSİM\nA: YAŞ\nS: BOY\nM: MENÜ")
else:
    print("işlem iptal edildi.")
    
    
while True: 
    print("Bu bir basit hesap makinasi\n1- Toplama\n2- Çıkarma\n3- Çarpma")
    
    select = input("Bir seçim belirtiniz 1/2/3: ")

    sayi = int(input("İLk sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    
    if select == "1":
        print('Toplama işlemi gerçekleştirildi: ', sayi + sayi2)
    elif select == "2":
        print("Çıkarma işlemi gerçekleştirildi: ", sayi - sayi2)
    elif select == "3":
        print("Çarpma işlemi gerçekleştirildi: ", sayi * sayi2)
    elif select == "4":
        break
        
# == eşit mi5 == 5 True
# != eşit değil mi 5 != 3 True
# > büyük mü 5 > 4 True
# < küçük mü 4 < 5 True
# >= büyük veya eşit mi 5 >= True
# <= küçük veya eşit mi 4 <= 8 True

d_age = input("yaşınızı giriniz: ")
driver_licanse = 18

if d_age >= str(driver_licanse):
    print("Ehliyet almaya yaşınız yetiyor.")
else:
    print("Ehliyet almaya yaşınız yetmiyor.")


# ATAMA OPERATÖRLERİ
# = değer ata
# += toplayıp ata
# -= çıkartıp ata
# *= çarpıp ata
# /= bölüp ata
# %= modunu alıp ata
# //= tam bölüp ata
# **= üssünü alıp ata

x = 20
x *= 5 
print(x)

cars = ["audi", "mercedes", "bmw"," citroen", "peugeot"]

car_select = input("Araç seçimini yapınız: audi\nmercedes\nbmw\ncitroen\npeugeot: ")
if car_select in cars:
    print("aradığınız marka liste de mevcut aranan:", car_select)
else:
    print("aradığınız marka liste de mevcut değil")
    
    
# if "audi" in cars:
#     print("audi arabalar listesin de mevcut. ")
# else:
#     print("audi arabalar listesin de mevcut değil.")


# kelime içerisinde arama
print("b" in "bmw")
# true döner çünkü bmw kelimesinin içerisinde b harfi vardır

a = [1, 2]
b = a # b burada a ya eşitlendi aynı değer oldu

print(a is b)
if a is b: 
    print("b a ya eşit")
else:
    print("b a ya eşit değil")

print(a)
print(b)


a = [1, 2]
b = [1, 2]

print(a == b) # true 
print(a is b) # false bellekte iki ayrı yer oluşturduğu için
b = a 
print(b is a) # true


#list metodlarıt
list = ["Yağız",  1.88, 2.03]
print(f"{list[0]}'ın boyu {list[2]} metredir.")
print(f"{list[1]}'un boyu {list[3]} metredir.")

# liste kopyalama 
list2 = ["kuru fasulye", "tavuk döner", "et döner"]
print(list2)
list3 = list2.copy()
print(list3)

#liste içerisinde değer ekleyip çıkarma
list3.append("mercimek corbası")
print(list3)
list3.remove("kuru fasulye")
print(list3)

#küçükten büyüğe sıralama
list4 = [1, 3, 5, 2 ,4]
list4.sort()
print(list4)

#büyükten küçüğe sıralama
list4.sort(reverse=True)
print(list4)

# sort()  = listeyi sıralar      
# sort(reverse=True) = büyükten küçüğe sıralanır 
# sorted() = orjinalini bozmadan sıralı liste oluşturur

# tupple veri türler

t_list = ("yağız",  "arda", "yağız") # tupple liste değiştirilemez sabittir 
print(t_list[0]) # 0 ile başlar -1 de listenin sonundaki elemanı alır

# count() methodu verinin kaç kez gezdiğini gösterir
print(t_list.count("yağız"))
# index elemanın kaçıncı index de olduğunu verie
print(t_list.index("yağız"))

t_list2 = ("yağız",  "arda")
for name in t_list2:
    print(name)
# tupple listesinin içeriisndeki ismleri sıralar

t_list3 = ("araba","uçak","gemi")
t_list_aranan = input("aradaığınız ulaşım aracını seçin: ")
if t_list_aranan in t_list3:
    print("belirtilen ulaşım aracı tupple listem de mevcut.")
else:
    print("aranan ulaşım aracı tupple listem de mevcut değil.")

#iç içe tupple
users = (
        ("yağız", 1.88),
        ( 2.03),
        ("arda", 1.84)
        )

print(f"{users[0][0]}'ın boyu {users[0][1]} metredir.")
print(f"{users[1][0]}'ın boyu {users[1][1]} metredir.")
print(f"{users[2][0]}'ın boyu {users[2][1]} metredir.")


#set küme elemanları
set_list = {"cig kofte", "sogan", "sarımsak", "cig kofte"}
print(set_list)
# cıktıda gözüktügü gibi tekrarlanan veriyi kaldırdı
set_list2 = {"cig kofte", "sogan", "sarımsak"}
#ekleme yapma (tekli)
set_list2.add("kuru sogan") # eklenen en başa geldi
print(set_list2)
# çoklu ekleme yapma
set_list2.update(["cacık", "et döner"])
print(set_list2)
# silme işlemi yapma klasik .remove() da hata verebilir .discard() kullanmak daha sağlıklı
set_list2.discard("et döner")
print(set_list2)
# .pop() ile rasgtele eleman sildirebilrisiniz
# .clear() bütün elemanları siler
# .copy() klasik kopyalar

for x in set_list2:
    print(x)
# bütün elemanları saydırır
 
# union iki kümedeki elemanları birleştirir ve tekrar edilenleri bir kez yazdırır
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
print(x.union(y))
#çıktı 1,2,3,4,5,6 olacaktır 2 veya daha fazla yazılan sayıları yazmayacak 1 kere yazacaktır

#intersection iki kümedeki ortak elemanları bulur örnek;
in_x = {1, 2, 3}
in_y = {3, 2, 1}
print(in_x.intersection(in_y))
# çıktı 1,2,3 olacaktır
# aldığımız çıktıyı büyükten küçüğe sıralayalım
in_y_ters = in_x.intersection(in_y)
print(sorted(in_y_ters, reverse=True)) 

#difference birinci kümede olup ikinci kümede olmayanı gösterir örnek;
dif_list = {2, 1, 3}
dif_list2 = {3, 4, 5 ,6}
print(dif_list.difference(dif_list2))
# çıktı 1, 2 olacaktır 1. küme de var fakat 2. küme de yok

#symmetric_difference ortak olanları çıkar
sy_list = {1, 2, 3}
sy_list2 = {1, 3, 5}
print(sy_list.symmetric_difference(sy_list2))
# çıktı 2,5 olur 1 ve 3 iki kümede de olduğu için çıkardı

#dict veri türleri
personel = {
        "yağız" : {
            "name": "Yağız",
            "age": 21,
            "size": 1.88 
            },
        "arda": {
            "name": "Arda",
            "age": 18,
            "size": 1.84   
            }
    }

print("İlk personel: ", personel["yağız"]["name"])
print("Üçüncü personel: ", personel["arda"]["name"])

# for x in personel:
#     if personel[x]["age"] >= 18:
#         print(personel[x]["name"], "Reşit")
#     else:
#         print(personel[x]["name"], "Reşit değil")

# stabil olan

for key, info in personel.items():
    if info["age"] >= 18:
        print(f"{info["name"]} reşittir")
    else:
        print(f"{info["name"]} reşit değildir")
        
#personel değerlerini verir
print(personel.values())

#değer ekleme
personel["yağız"].update({"şehir": "Ankara"})
#tek öğrenci sorgulama
print(personel["yağız"])
# .copy() kopyalama
# .popitem() son eklenen anahtar değerini siler

# sadece değerleri yazdırır
for d in personel.values():
    print(d)

# keysleri yazdırır
for keys in personel:
    print(keys)
    
# keys ve değerleri yazdırır
for keys, deger in personel.items():
    print(keys, ":", deger)

# .upper() yazıyı büyültür
# .lower() yazıyı küçültür
# .title() kelimenin baş harflerini büyültür
# .capitalize() kelimenin ilk harfini büyültür
# .strip() boşlukları siler
# .replace() metinde değişiklik yaptırır
text = "ben arabaları çok seviyorum"
print(text.replace("çok seviyorum", "sevmiyorum"))
# çıktı ben arabaları sevmiyorum olacaktır.
# .split() metini listeye çevirir
print(text.split())
# çıktı ['ben', 'arabaları', 'çok', 'seviyorum'] olacaktır
# .join() listeyi string hlaine getirir
names = ["yağız", "arda"]
print(",".join(names))
# çıktı yağız,umut,arda olacaktır
# .find() metnin geçtiği indexi verir
# .count() kaç kere geçtiğini verir
# .startswith() belirli bir ifadeyle baslıyomu
# .startswith() belirli bir ifadeyle bitiyormu
# .isalpha() sadece harflerden mi oluşuyor
# .isdigit() sadece rakamlardan mı oluşuyor
# .isalnum() sadece rakam ve harftenmi oluşuyor
# hepsinin kullanım şekli print("fenotip", .isalpha())

#0 dan başla 21 e kadar ikişer ikişer attır
for i in range(0,21,2):
    print(i)



attc = open("slm.txt", "w")
attc.write(personel.values())
attc.close()

personel["yağız"].update({"şehir": "Ankara"})
personel["arda"].update({"şehir": "istanbul"})

with open("slm.txt", "w", encoding="utf-8") as atch:
    for names, info in personel.items():
        atch.write(f"name: {names}\n")
        for keys, dgr in info.items():
            atch.write(f" {keys} : {dgr}\n")
            


    