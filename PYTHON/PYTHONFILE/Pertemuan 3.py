# Operation arimatika ==> Module
# Operation logika

# print (25 % 2)
# print (13 % 2)
# print (14 % 2)
# print (15 % 2)
# print (16 % 2)
# print (17 % 2)

# print(12%2 == 0)
# print(13%2 == 0)
# print(14%2 == 0)
# print(15%2 == 0)
# print(16%2 == 0)
# print(17%2 == 0)

# Programnya 
# a = 10 % 15

# if a > 0:
#     print(a, "Lebih dari nol")
#     if a == 5:
#         print(a, "sama dengan lima")
#     print("mau keluar dari if")

# print("Program selesai")

# Flowcart

# angka = input("Masukan uang kamu sekarang: ")
# angka = int(angka)

# if angka < 0:
#     print("gk punya uang, punyanya utang")
#     print("Kamu punya utang ya???")
# elif angka == 0:
#     print("Ya gk punya uang!!!")
# else:
#     print("Punya uang")
#     print("Holang kaya!!!")
# print("Demikian keadaan uang kamu sekarang :) ")

# Flowcart
# angka = int(input("Masukan angka kamu: "))
# angka = angka % 2

# if angka == 0:
#     print("Genap")
# else:
#     print("Ganjil")

# print("Program selesai")

# While 
# i = 1
# while i < 6:
#   print(i)
#   i += 1

# Program inputnya
# angka = int(input("Angka: "))
# while angka < 1000:
#     angka = angka + 1
#     if angka % 2 == 0:
#         print(angka, "adalah Bilangan Genap")
#     else:
#         print(angka, "adalah Bilangan Ganjil")
# print("Program selesai")

angka = int(input())
kalimat = "Boy"

if(angka < 0):
    kalimat += "Bad"
    if(angka % 2 == 0):
        kalimat = kalimat + "Beni"
    elif(angka % 2 == 1):
        kalimat = kalimat + "Boy"
else:
    if(angka % 2 == 0):
        kalimat = kalimat + "Beni"
    elif(angka % 2 == 1):
        kalimat = "Budi" + kalimat 
    else:
        kalimat = "Becca"
    kalimat = kalimat + "Billiard" + kalimat

if(len(kalimat) > 5):
    kalimat = kalimat + "s"
    if(angka - 10 > 0):
        kalimat = "Becca" + kalimat
    else:
        kalimat = kalimat + "Becca"
elif(len(kalimat) < 5):
    kalimat + "Belly" + kalimat

print(kalimat)



# angka = int(input("Masukan angka:"))
# hasil = False
# tipe = ""
# if angka == 0:
#     angka /= 2
#     tipe += "A"
# elif angka < 0:
#     angka *= 2
#     hasil = (angka % 5) % 2 == 0
#     tipe += "B"
# else:
#     angka += 10
#     tipe = "C"
#     if angka > 0:
#         hasil = angka < 100
#         tipe += "D"
#     else:
#         hasil = angka >= -25
#         tipe += "E"
# if hasil and (angka % 2 == 0):
#     hasil = hasil or (angka > 0)
#     tipe += "F"
# else:
#     hasil = not hasil and angka % 2 == 0
#     tipe += "G"
# print(tipe)    

# angka = int(input("MAMAH NGASIH UANG KE ANDI BERAPA : "))
# tipe = ""
# if angka > 100000:
#     angka -= 80000
#     tipe += "Andi pergi ke Matahari\n"
#     if angka > 100000:
#         angka -= 75000
#         tipe += "Andi pergi ke Indomaret\n"
#     else:
#         angka -= 5000
#         tipe += "Andi pergi ke pasar\n"
# elif(angka < 100000 and angka >= 50000):
#     angka -= 75000
#     tipe += "Andi pergi ke Ramayana\n"
# else:
#     angka -= 25000
#     tipe += "Andi pergi ke Victoria\n" 
# if angka > 20000:
#     angka -= 10000
#     tipe += "Andi ke warung"
# else:
#     tipe += "Andi langsung pulang"
# print(tipe)
# print("Sisa Uang andi: ", angka)
# sisa_uang = angka
# situasi = ""
# if sisa_uang > 10000:
#     situasi += "Andi balikin sisa uang ke ibu\n"
# else:
#     situasi += "duit nya andi simpen di celengan\n"

# print(situasi)


# print("4" + "10")

# WHILE MENGECEK TERUS MENERUS BILA BILANGAN TRUE

# a = int(input("Masukan angka:"))
# c = 1
# while (c <= a):
#     print("Looping ke:", c)
#     c += 1




# a = True
# b = 0

# while a:
#     b += 2
#     print(b, end=", ")
#     if (b < 100):
#         pass
#     else:
#         a = False   

# a = 0
# b = 1
# while True:
#     b += 2
#     if (not b < 100):
#         break

# a = 0
# while True:
#     a += 1
# a = 100   
# while a > 0:
#     a -= 1
#     b = 0
#     while b < 5:
#         print(a, b)
#         b += 1  
#         c = 10   
# Pengulangan ini hasilnya ada 2 tempat yaitu while pertama itu hasilnya berada disebelah kiri (while a > 0:)
# While selanjutnya (while b < 5) hasilnya berada di sebelah kanan
# atau kata lain looping atau while juga dapat beranak pinak atau di dalam loop atau while bisa ada loop atau while juga





















































































































































































