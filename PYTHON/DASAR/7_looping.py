# Looping merupakan sebuah cara untuk melakukan perulangan pada blok program
# setiap perulangan tersebut disebut sebagai iterasi
# terdapat dua jenis looping yaitu :
# while (saat)
# for (untuk)

# penulisan perulangan mirip seperti if statement (branching) dimana setiap
# blok program perulangan akan memiliki gerbang pengujian dan blok program

a = 0
while a < 10:
    
    print(a)
    a += 1
    
print("Selesai")

# contoh program di atas saat di jalankan adalah sebagai berikut :
# pendefinisian a = 0 pada baris 10
# a di cek pada gerbang while dengan kondisi a < 10;
# saat a = 0, a < 10 akan true, sehingga akan membaca blok program while
# yaitu pada baris 12, melakukan penambahan (increment) satu angka pada a
# kemudian pada baris 13 melakukan print a, saat ini karena a telah di increment,
# maka print(a) akan menghasilkan nilai 1
# karena blok ini merupakan blok looping, maka dari ini, program akan
# kembali lagi membaca ke posisi gerbang dari looping tersebut, yaitu
# pada baris 11 dengan data yang telah diubah sebelumnya, sehingga a = 1
# saat dilakukan pengecekkan a < 10 akan menghasilkan true, sehingga masuk
# kembali kedalam blok program dan membaca baris 12, 13
# dilakukan lagi penambahan satu angka sehingga menjadi a = 2
# dan seterusnya akan di lakukan iterasi sampai a menyentuh a = 9
# kemudian saat masuk akan di lakukan penambahan satu angka yaitu a = 10
# saat program kembali membaca kondisi while, saat ini karena a = 10
# maka a < 10 akan menghasilkan false, kemudian program akan langsung
# loncat pada baris 15, menyatakan bahwa print Selesai, hal ini terjadi
# seperti pada if yaitu jika kondisi false maka program akan di lewat (bypass).

a = 10

while a > 0:
    a -= 1
    b = 0
    while b < 5:
        print(a, b)
        b += 1
        
        
# 9 0
# 9 1
# 9 2
# 9 3
# 9 4
# 8 0
# 8 1
# ...
# 1 4

# sama seperti branching, pada looping juga dapat mengimplementasikan nested
# atau beranak pinak, yaitu di dalam while terdapat while atau
# di dalam loop ada loop

# di bawah ini merupakan contoh looping yang digunakan untuk menampilkan garis
# bilangan angka genap di bawah 100

a = True
b = 0
while a:
    b += 2
    print(b, end=", ")
    if(b < 100):
        pass
    else:
        a = False
    
# while juga dapat menerima input variabel dengan data berupa boolean.
# pada contoh di atas a = True, sehingga while akan di jalankan
# setiap perulangan akan melakukan penambahan dan menampilkan nilai pada variabel b
# ada bagian branching disini, dimana saat b < 100 dijalankan pass, sehingga
# program akan melakukan iterasi lagi, tetapi jika b >= 100, maka akan memiliki
# kondisi False pada gerbang if, menyebabkan a = False, kemudian saat
# dilakukan iterasi kembali, a akan menjadi False pada gerbang while,
# sehingga program keluar dari blok program while tersebut.

b = 0
while True:
    b += 2
    print(b)
    if((not b < 100) or b == 50):
        break
    
# 2
# 4
# ...
# 50
    
# dengan output yang sama, yaitu untuk menampilkan angka genap di bawah 100,
# program di atas menggunakan perintah break, untuk keluar dari looping
# break akan memaksakan keluar dari looping, walaupun pada gerbang while
# data tidak berubah sama sekali menjadi False

a = -1
while True:
    a += 1
    print("Awal")
    if(a % 2 == 0):
        print(a, "Genap")
        continue
    elif(a < 100):
        break
    else:
        print(a, "Ganjil")
    print("Muter")
    
# Awal
# 0 Genap
# Awal

# perintah selanjutnya adalah continue, yaitu melanjutkan iterasi looping
# pada kondisi saat membaca gerbang if pada baris 84, jika saat kondisi nya True
# maka akan di baca baris 85, dan 86.
# saat membaca 86, normalnya program akan keluar dari if, dan loncat untuk membaca
# bagian baris 91, karena menggunakan perintah continue,
# maka program akan langsung loncat kembali pada gerbang while pembuka nya sehingga
# akan kembali melakukan pembacaan kondisi pada baris 81.

a = 0
while a < 10:
    print("Angka ke",a, sep="-")
    a += 1
    
# program di atas adalah untuk menampilkan angka dari 0 sampai 9 (sebelum 10)
# bisa di sederhanakan menggunakan jenis loop selanjutnya, yaitu for loop

for a in range(0, 10, 2):
    print("Angka ke",a, sep="-")

# dengan sintaks di atas, penulisan semakin mudah, karena
# setiap iterasi atau perulangan secara otomatis akan melakukan penambahan nilai
# sebanyak 1 (increment +1) dengan nilai a kondisi awal adalah a = 0
# dan dilakukan berulang sampai kondisinya < 10. sehingga output yang di tampilkan sama dengan
# program sebelumnya.
# format penulisannya adalah sebagai berikut

# for nama_variabel in range(nilai_maksimum):
#   blok program
# for = untuk
# in = dalam
# range = jenjang/jangka

for i in range(5, 10):
    print(i)
    
# angka 5 menjadi angka pertama
# angka 10 menjadi angka terakhir\
    
    
# 5
# 6
# 7
# 8
# 9

# untuk penulisan seperti contoh di atas,
# bahwa range akan di mulai dari 5
# dan di akhiri di < 10, sehingga berakhir di 9
# format penulisannya adalah sebagai berikut

# for nama_variabel in range(minimum, maksimum):
#   blok program

# dalam sintaks looping for juga, kita dapat melakukan
# break dan continue, yang menjadi perbedaan
# mendasar adalah bawha looping for adalah melakukan increment
# terhadap sebuah variabel looping wajib di setiap iterasinya.

# perlu di ingat, terhadap variabel pada blok program



# x     n    y    z     k
# 10    0    0    0     10
# 10    1    1    1     ~   
# 10    2    3    0     10
# 10    3    6    1     ~
# 10    4    10   0     10
# 10    5    15   1     ~
# 
# 10    9    45

# 0
# 0 0
# 1
# 1 0

# 9 0
# 45

# contoh di atas merupakan penggambaran dari blok program
# variabel x dapat di baca di luar dan di dalam blok program for,
# begitu juga dengan variabel y. tetapi, untuk variabel z
# karena tidak pernah di definisikan di luar blok looping, maka
# variabel z hanya dapat di baca di dalam for loop tersebut,
# atau di dalam if. begitu juga dengan variabel n
# yang hanya bisa di baca di dalam.
# variabel k hanya dapat dibaca di dalam blok program if, tidak
# dapat di baca di luar blok program if, walaupun masih di dalam for loop
# apa lagi di luar looping, tidak mungkin dapat terbaca.

# jika variabel di definisikan hanya di dalam blok program,
# maka data atau isi dalam variabel tersebut tidak dapat di baca
# pada blok yang lebih tinggi atau yang lebih luar (unbound)

# x <- di luar | dapat di baca di dalam for, dapat di baca di dalam if
# y <- di luar | dapat di baca di dalam for, dapat di baca di dalam if
# n <- di dalam for | dapat di baca di dalam if
# z <- di dalam for | dapat di baca di dalam if
# k <- di dalam if | hanya di baca di dalam if

for i in range(50, 100, 2):
    print(i)
    
# program di atas adalah menampilkan angka genap
# mulai dari i = 50, sampai dengan i < 100
# hal ini dapat di lakukan , karena atribut ketiga dari fungsi range
# adalah banyaknya penambahan yang dilakukan pada setiap iterasi
# angka 2 disini sebagai jarak atau penambah bilangan

for i in range (-50, -100, -2):
    print(i)
    
# berikut contoh lainnya yaitu angka genap negatif
# dimulai dari -50 sampai dengan i < -100
# setiap perulangan dilakukan -2 sama seperti i -= 2

# berikut ini ringkasan penggunaan range pada for loop
# range(10) <- menghitung dari 0 sampai 9, dengan pertambahan 1 setiap iterasi
# 0,1,2,3,4,5,6,7,8,9
# range (5, 10) <- menghitung dari 5 sampai 9, dengan pertambahan 1 setiap iterasi
# 5,6,7,8,9
# range (5, 10, 2) <- menghirung dari 5 sampai 9, dengan pertambahan 2 setiapn iterasi
# 5,7,9

# berikut ini penulisan yang bersesuaian antara while dan for loop
# menampilkan angka ganjil dibawah 50:

a = 1
while (a < 50):
    print(a)
    a += 2

# dalam bentuk for loop

for a in range(1, 50, 2):
    print(a)
    
# menampilkan hasil perkalian lima sampai 5 * 20 :

a = 0
while(a < 20):
    print(a * 5)
    a += 1
    
# dalam for
for a in range(20):
    print(a * 5)
    
# contoh perulangan untuk membentuk segi tiga :
tinggi = 20
for t in range(tinggi):
    for l in range(tinggi * 2):
        karakter = ""
        if l == (tinggi - 1) - t:
            karakter = "/"
        elif (tinggi * 2) - l == tinggi - t:
            karakter = "\\"
        else:
            if(t == tinggi - 1):
                karakter = "_"
            else :    
                karakter = " "
        print(karakter, sep="", end="")
    print()
    
# cara menjalankan program ini
# python 7_looping.py
# ekspektasi dari hasil program ini
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Selesai
# 9 0
# 9 1
# 9 2
# 9 3
# 9 4
# 8 0
# 8 1
# 8 2
# 8 3
# 8 4
# 7 0
# 7 1
# 7 2
# 7 3
# 7 4
# 6 0
# 6 1
# 6 2
# 6 3
# 6 4
# 5 0
# 5 1
# 5 2
# 5 3
# 5 4
# 4 0
# 4 1
# 4 2
# 4 3
# 4 4
# 3 0
# 3 1
# 3 2
# 3 3
# 3 4
# 2 0
# 2 1
# 2 2
# 2 3
# 2 4
# 1 0
# 1 1
# 1 2
# 1 3
# 1 4
# 0 0
# 0 1
# 0 2
# 0 3
# 0 4
# 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, Awal
# Angka ke-0
# Angka ke-1
# Angka ke-2
# Angka ke-3
# Angka ke-4
# Angka ke-5
# Angka ke-6
# Angka ke-7
# Angka ke-8
# Angka ke-9
# Angka ke-0
# Angka ke-1
# Angka ke-2
# Angka ke-3
# Angka ke-4
# Angka ke-5
# Angka ke-6
# Angka ke-7
# Angka ke-8
# Angka ke-9
# 5
# 6
# 7
# 8
# 9
# 0
# 0 0
# 1
# 2
# 2 0
# 3
# 4
# 4 0
# 5
# 6
# 6 0
# 7
# 8
# 8 0
# 9
# 45
# 50
# 52
# 54
# 56
# 58
# 60
# 62
# 64
# 66
# 68
# 70
# 72
# 74
# 76
# 78
# 80
# 82
# 84
# 86
# 88
# 90
# 92
# 94
# 96
# 98
# -50
# -52
# -54
# -56
# -58
# -60
# -62
# -64
# -66
# -68
# -70
# -72
# -74
# -76
# -78
# -80
# -82
# -84
# -86
# -88
# -90
# -92
# -94
# -96
# -98
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
# 21
# 23
# 25
# 27
# 29
# 31
# 33
# 35
# 37
# 39
# 41
# 43
# 45
# 47
# 49
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
# 21
# 23
# 25
# 27
# 29
# 31
# 33
# 35
# 37
# 39
# 41
# 43
# 45
# 47
# 49
# 0
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# 55
# 60
# 65
# 70
# 75
# 80
# 85
# 90
# 95
# 0
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# 55
# 60
# 65
# 70
# 75
# 80
# 85
# 90
# 95
#                    /\
#                   /  \
#                  /    \
#                 /      \
#                /        \
#               /          \
#              /            \
#             /              \
#            /                \
#           /                  \
#          /                    \
#         /                      \
#        /                        \
#       /                          \
#      /                            \
#     /                              \
#    /                                \
#   /                                  \
#  /                                    \
# /______________________________________\