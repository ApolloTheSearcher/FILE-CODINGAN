# a = True
# b = 0
# while a:
#     b += 2
#     print(b, end=", ")
#     if(b < 100):
#         pass
#     else:
#         a = False

# b = 0
# while True:
#     b += 2
#     print(b)
#     if((not b < 100) or b == 50):
#         break
    
    
    
    
# a = -1
# while True:
#     a += 1
#     print("Awal")
#     if(a % 2 == 0):
#         print(a, "Genap")
#         continue
#     elif(a < 100):
#         break
#     else:
#         print(a, "Ganjil")
#     print("Muter")


# for i in range (10):
#     print("Angke ke", i, sep = "-")


# for i in range(5, 10, 2):
#     print(i)


# for i in range(-100, 2):
#     print(i)



tinggi = 5
for m in range (tinggi):
    for n in range (tinggi):
        karakter = " "
        # if (n == 0 and m == 0) or (n == (tinggi - 1) and m == 0) or (n == (tinggi - 1) and m == (tinggi - 1)) or (n == 0 and m == (tinggi - 1)):
        #     karakter = "X"
        if (n == 0 or m == 0 or m == (tinggi - 1) or n == (tinggi - 1)):
            karakter = "O"
            
        print(karakter, end=" ")
    print()

# def kalkulator (a, b):
#     tambah = a + b
#     kurang = a - b
#     kali = a * b
#     bagi = a / b
#     print("Nilai pertambahannya: ", tambah)
#     print("Nilai perkurangan: ", kurang)
#     print("Nilai perkalian: ", kali)
#     print("Nilai pembagian: ", bagi)
# kalkulator(int(input("Masukan angka a:")), int(input("Masukan angka b:")))
# BLOK PROGRAM DI ATAS KALKULATOR TANPA RETURN


# def kalk (a, b):
#     tambah = a + b
#     kurang = a - b
#     kali = a * b
#     bagi = a / b
#     return tambah, kurang, kali, bagi
# tambah, kurang, kali, bagi = kalk (int(input("Nilai pertama:")), (int(input("Nilai kedua:"))))

# print(" Nilai pertambahannya:", tambah, "\n Nilai perkurangan:", kurang, "\n Nilai perkalian:", kali, "\n Nilai pembagian:", bagi)

#BLOK PROGRAM DIATAS MENGGUNAKAN RETURN


# LIST
# angka = []
# for i in range(1, 100, 2):
#     angka.append(i)

# Sn = 0
# for data in angka:
#     Sn += data
    
# print(Sn)

# Hint 
# bikin himpunan ( {} ) <======= lambang himpunan
# si himpunan nya di isi dari dua sampai maksimum menggunakan for sama append
# looping menguji seluruh angka yang tidak di eliminasi
# si angka yang di uji di cari faktornya, jadi dia loncat-loncat sesuai angka
#  contoh: range(angka_penguji * 2, angka_max, angka_penguji)
#  si index itu di jadiin nol
#  contoh: angka[i] = None
#  menguji angka selanjutnya harus ngecek apakah itu None atau enggak, kalo gak None







# siswa = [{ 
#           "Nama" : "Gentha Ardaana",
#           "NIS" : 12331241242422,
#           "Alamat" : ("Cibadak", "Sukabumi"),
#           "Tanggal lahir" : (27, 1, 2005),
#           "Kelas" : (11, True, 3)},
#          { 
#           "Nama" : "Fitri Juki",
#           "NIS" : 12333422990112,
#           "Alamat" : ("Cijalingan","Sukaraja"),
#           "Tanggal Lahir" : (10, 11, 2003),
#           "Kelas" : (10, False, 3)},
#          { 
#           "Nama" : "Juki Aksan",
#           "NIS" : 1223981912029,
#           "Alamat" : ("Pelabuhan, Sukabumi"),
#           "Tanggal Lahir" : (5, 9, 1992),
#           "Kelas" : (12, True, 9),}]
# namaBulan = ["Januari",
#              "Febuari",
#              "Maret",
#              "April"
#              "Mei",
#              "Juni",
#              "Juli",
#              "Agustus",
#              "September",
#              "Oktober",
#              "November",
#              "Desember"]
# for i in range (len(siswa)):
#       dataSiswa = siswa[i]
#       kec,kab = dataSiswa["Alamat"]
#       tanggal, bulan, tahun = dataSiswa["Tanggal Lahir"]
#       kelas, ipaips, nomor = dataSiswa["Kelas"]
#       print("NAMA", dataSiswa["Nama"], sep="\t \t: ")
#       print("NIS", dataSiswa["NIS"], sep = "\t \t: ")
#       print("Alamat",kec + " " +kab, sep = "\t \t: ")
#       print("Tanggal Lahir",str(tanggal) + " " + namaBulan[bulan-1] + " " + str(tahun), sep = "\t: ")
#       print("Kelas", str(kelas) + " " +
#             ("IPA" if (ipaips) else "IPS")
#             + " " + str(nomor),sep = "\t\t: ")
#       dataSiswa["umur"]= 2022 - tahun
#       print("Umur", dataSiswa["umur"], sep ="\t\t: " )
#       print()









