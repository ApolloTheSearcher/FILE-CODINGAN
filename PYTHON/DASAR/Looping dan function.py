# a = int(input("Masukan angka:"))
# while True:
#     a += 1
#     print("angka awal")
#     if (a % 2 == 0):
#         print(a, "Genap")
#         continue
#     elif ( a < 1000):
#         break
#     else:
#         print(a, "Ganjil")
#     print("Muter")
    
# print("Program selesai")


# keadaan diatas menggambarkan looping dengan menggunakan keadaan logical expresion
# dimana bila kita memasukan akan maka akan True jika kita memasukan selain int melainkan memasukan str maka code while tidak terlaksanakan tetapi langsung
# print ke program selesai
# jika kita memasukan angka (int) maka:
# angka akan ditambah 1 ( += 1)
# kemudian keadaannya akan dilihat , jika angka yang dimasukan dan ditambahkan bermod 2 akan sama dengan 0 maka dia akan menghasilkan angka yang diketika += 1 dan str "Genap"
# Jika angka tidak tetapi angka kurang dari 1000 maka program akan break atau berhenti
# Jika tidak di antara keduanya program akan berada di posisi else dan akan menghasilkan (angka, Ganjil) dan akan terus berputer atau muter ke atas
# bila bilangan dapat menembus elif atau dapat berada di else maka angka yang dimasukan akan terus berjalan hingga tak terhingga hasilnya
# COBA AJA LOH KALO MISALNYA MAU DAN GK PANIK!!!

# a = int(input("Angka yang mau dimasukan pertama kali: "))
# b = int(input("Angka yang digunakan sebagai pembatas angka pertama: "))
# while a < b:
#     print("Angka ke", a, sep="-")
#     a += 1
# jadi kesimpulan pada program diatas ini yaitu jadi selagi angka yang dimasukan pertama tidak lebih dari angka yang dimasukan sebagai pembatas
# maka dia akan terus ditulis dan kemudia angka tersebut ditambahkan dengan 1 sehingga angka terus bertambah
# dan akan menghasilkan angka ke, angka yang dimasukan atau angka yang dimasukan pertama lalu di tambah 1 
# karena pada perogram terdapat (sep=) jadi nanti itu ditambahkan kedalam kalimat angke ke sebagain string (atau kita sebut saja itu sebagai parameternya)
# kemudian angka terus bertambah hingga angka yang dimasukan dan angka yang dimasukan ditambah 1 tidak melebih angka yang dimasukan sebagai pembatas angka pertama
# Parameter adalah variable yang mampu menampung nilai untuk diproses didalam fungsi

# for a in range (10):
#   print(a)
    
# pada code seperti ini (for in range) adalah cara mudah yang digunakan untuk melakukan looping atau bisa kita sebut sebagai versi mudahnya dari looping
# pembahasan untuk code:
# for a in range (10) atau dapat kita artikan dengan for namA_variablE in range (nilaI_maksimuM):
#|||||||||||||||| BLOK PROGRAM DIATAS DISEBUTNYA ||||||||||||||||

# atau code yang digunakan:

# for a in range (5,100):
#     print (a)
    
# pembahasan untuk code:
# for namA_variabLe in range (niLai_minImum, nilaI_maksimuM):
#|||||||||||||||| BLOK PROGRAM DIATAS DISEBUTNYA ||||||||||||||||
# dengan code seperti ini bahwa nanti si variable a akan menghasilkan nilai yaitu jangka dari awalnya 5 kemudian angka berhenti hingga angka nya kurang dari angka maksimum
 
# for = untuk
# in = dalam
# range = jenjang / jarak

# x = 10
# y = 0
# for n in range(x):
#     print (n)
#     y += n
#     z = n % 2
#     if (z == 0):
#         print(n, z)
#         k = 10

# print(y)

# PENJELASAN TERHADAP BLOK DIATAS !!!!!!!!!!
# jadi program di atas termasuk BLOK PROGRAM
# jadi kan x dan y nilai variable nya sudah tertera
# nah pada blok program looping for in range itu bila huruf atau nama variable tidak diketahui maka dapat kita asumsikan bahwa variable itu bernilai (0)
# maka program diatas bahwa for n in range (x) yaitu nilai variable n akan dihasilkan hingga jarak nilai x (10)
# setelah kita tau nilai n maka nilai n akan terus diproses untuk menghasilkan nilai y yaitu dengan menambahkan dirinya untuk variable n
# kemudian pada baris ke 67 itu kita akan mengetahui nilai variable dari z yaitu dengan memod 2 kan nilai n
# pada baris 68 jika nilai z sama dengan 0 ( nilai variable z itu hasil dari n mod 2)
# maka akan menghasilkan nilai dari variable n, nilai variable dari z)
# variabel k hanya dapat dibaca di dalam blok program if, tidak
# dapat di baca di luar blok program if, walaupun masih di dalam for loop
# apa lagi di luar looping, tidak mungkin dapat terbaca.
# jika variabel di definisikan hanya di dalam blok program,
# maka data atau isi dalam variabel tersebut tidak dapat di baca
# pada blok yang lebih tinggi atau yang lebih luar (unbound)

# posisi pada setiap nama variable pada blok program diatas
# x <- di luar | dapat di baca di dalam for, dapat di baca di dalam if
# y <- di luar | dapat di baca di dalam for, dapat di baca di dalam if
# n <- di dalam for | dapat di baca di dalam if
# z <- di dalam for | dapat di baca di dalam if
# k <- di dalam if | hanya di baca di dalam if


# contoh blok program yang lain


# for n in range (5, 100, 2):
#     print(n)

# Blok program diatas menjelaskan bahwa terdapat tiga jenis atau simpelnya yaitu:
# for namA_variablE in range (nilaI_minimuM, nilaI_maksimuM, Bilangan Genap atau Ganjil atau bilangan yang digunakan untuk iterasi)
# Program tersebut  menjelaskan variable i bahwa setiap bilangan yang berawal dari 5 hingga 100 akan bercabang atau beriterasi dengan 2 ( bilangan iterasinya)


# Menampilkan perkalian lima sampai 5 * 20:

# contoh yang menggunakan while
# a = 0
# while (a < 20):
#     print(a * 5)
#     a += 1

# contoh yang menggunakan for in range

# for a in range (20):
#     print(a * 5)

# ternyata guys for in range juga dapat beranak pinak seperti while dan dapat menggunakan logical expresion atau didalam for in range dapat diisi dengan logical expresion
# # contoh perogram for in range yang beranak pinak:

# tinggi = 5
# for t in range(tinggi):
#     for l in range(tinggi * 2):
#         karakter = ""
#         if l == (tinggi - 1) - t:
#             karakter = "/"
#         elif (tinggi * 2) - l == tinggi - t:
#             karakter = "\\"
#         else:
#             if(t == tinggi - 1):
#                 karakter = "_"
#             else :    
#                 karakter = " "
#         print(karakter, sep="", end="")
#     print()

# tinggi = 10
# for t in range(tinggi):
#     for l in range (tinggi):
#         karakter = " "
#         if (t == 0 and l == 0 ) or (l ==(tinggi - 1) and t ==(tinggi -1) or (l == (tinggi - 1) and t == 0) or (t == (tinggi - 1) and l == 0)):
#             karakter = "o"
#         elif t == 0 or t == (tinggi - 1):
#             karakter = "-"
#         elif l == 0 or l == (tinggi - 1):
#             karakter = "|"
#         elif t == l:
#             karakter = "\\"
#         elif t == (tinggi - 1) - l:
#             karakter = "/"
#         print( karakter, sep= " ", end=" ")
#     print( )
    
    
# Karakter untuk spasi disini untuk menghemat karena else akan ngeprint spasi pada blok program diatas
        
# BLOK PROGRAM SEGITIGA KEBALIK
   
# tinggi = 5
# for t in range (tinggi):
#     for l in range (tinggi * 2 - 1):
#         karakter = " "
#         if l >= t and l < (tinggi * 2)- t - 1:
#             karakter = "o"
#         print(karakter, end = " ")     
#     print()





# BAB FUNCTION
def cekAngkaGanjil(angka):
    if(angka % 2 == 0):
        print(angka, "adalah Genap")
    else:
        print(angka, "adalah Ganjil")
        
cekAngkaGanjil(int(input("Masukan Angka apa aja:")))
        
angka = 10

def namaSaya():
    print("admin")
    
    
for i in range (10):
    namaSaya()



# Contoh blok program funcition
def cekAngka(a, b):
    if (a > b):
        print(a, "lebih besar dari", b)
    elif ( a == b ):
        print(a, "sama dengan nilai dari", b)
    else:
        print(a, "lebih kecil dari", b)
        
cekAngka( 3, 8)


# contoh blok program yang lain

def pesan (nama, prefix = "Hallo" ):
    print(prefix + ",", nama)
    
pesan("Admin")
pesan(nama = "Admin2")
pesan("Admin3", "Hallo")
pesan(prefix = "Hola", nama = "Admin 4")
hasil = pesan("Admin")
print(hasil)



# Contoh blok program lagi mengenai funcition
# MENGGUNAKAN RETURN


def pertambahan (a, b):
    hasil = a + b
    return hasil
output = pertambahan (9, 4)
print(output)
print(pertambahan(10, 12))


# sintaks return akan mengembalikan nilai untuk keluaran (output) fungsi
# Dengan menggunakan output disini output digunakan untuk mengganti nama variable pada pertambahan sehingga ketika kita ingin memunculkan hasilnya
# kita tinggal print outputnya saja
# Return digunakan untuk menggantikan print atau mempersingkat proses print pada blok program penjumlahan

# contoh blok program function yang menggunakan return dan contoh input angka dengan funcition

angkaMasuk = int(input("Masukan Angka:"))
def cekAngka (a):
    if (a > 0):
        return "Positif"
    elif (a < 0):
        return "Negatif"
    else:
        return "Nol"
print(cekAngka(angkaMasuk))

# Return disini digunakan untuk melakukan penyimpanan data


# Contoh blok program function untuk menghasilkan bagi dan sisa dengan menggunakan input (kalkulator sederhana untuk menentukan bagi dan sisa dengan memasukan dua angka)

def bagiSisa (a, b):
    if(b == 0):
        return None, None
    else:
        bagi = a / b
        sisa = a % b
        return bagi, sisa
    
bagi, sisa = bagiSisa (int(input("Masukan angka a: ")), int(input("Masukan angka b: ")))
if (bagi == None or sisa == None):
    print("Bilangan tidak boleh nol")
else:
    print("Bagi :", bagi)
    print("Sisa :", sisa)







































































