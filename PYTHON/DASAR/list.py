# himpunanAngka = [4,2,3,6,4,2,1]
# himpunanNama = ["Adi", "Ferdi","Riski","Fernan", "Kevin"]
# print(himpunanAngka)
# print(himpunanNama)
# print(himpunanNama[2:3])
# print(himpunanAngka[2:-2])

# himpunanAngka = [4,2,1,3,6,5,4,7]
# # print(himpunanAngka[2:-2])
# for i in range(len(himpunanAngka)-1, -1 ,-1):
# # len disini untuk menghitung jumlah angka pada list atau jumlah sesuatu di dalam list
#     print(himpunanAngka[i])
    
# u = []
# for i in range (1,20,2):
#     u.append(i)
# print(u[-3:])
# append pada python di list berguna untuk menambahkan kalimat atau objek ke dalam list
# Array itu himpunan lebih dari 1 dalam 1 variable
# List itu menghasilkan semua bilangan yang ada di dalam kurung [] sedangkan
# Set itu menghasilkan angka yang belum ada di dalam kurung {}
# Map pake kurung kurawal {} tapi indeksnya berbeda
# Didalam Map itu ada key di gunakan untuk kuncinya dan value untuk datanya
# List untuk menambah bilangan dengan menggunakan append
# Set untuk menambakan bilangan yang belum ada yaitu add
# s = {1,2,3,4,5,6,7,8,8}
# print(s)
# s.add(10)
# print(s)

# # TUPLE

# tanggalLahir = 21,1,5
# tanggal, bulan, tahun = tanggalLahir
# print(tanggalLahir)
# xyz = 1,5,10
# x,y,z = xyz
# print(x)
# print(z)
# print(y)
# print(xyz)
# xz = x,z
# print(xz)




# dataSiswa = {"nama" : "Gentha Ardaana",
#              "NIS"  : 1233142124141242,
#              "Alamat" : ("Cibadak", "Sukabumi"),
#              "Tanggal Lahir" : (27,1,2005),
#              "Kelas" : (11, True, 3),
#              }
# kec,kab = dataSiswa["Alamat"]
# tanggal, bulan, tahun = dataSiswa["Tanggal Lahir"]
# namaBulan = ["Januari",
#          "Febuari",
#          "Maret",
#          "April",
#          "Mei",
#          "Juni",
#          "Juli",
#          "Agustus",
#          "September",
#          "Oktober",
#          "November",
#          "Desember"]
# kelas, ipaips, nomor = dataSiswa["Kelas"]
# print(dataSiswa)
# print("NAMA", dataSiswa["nama"], sep="\t \t: ")
# print("NIS", dataSiswa["NIS"], sep = "\t \t: ")
# print("Alamat",kec + " " +kab, sep = "\t \t: ")
# print("Tanggal Lahir",str(tanggal) + " " + namaBulan[bulan-1] + " " + str(tahun), sep = "\t: ")
# print("Kelas", str(kelas) + " " +
#       ("IPA" if (ipaips) else "IPS")
#       + " " + str(nomor),sep = "\t\t: ")
# dataSiswa["umur"]= 2022 - tahun
# print("Umur", dataSiswa["umur"], sep ="\t\t: " )
# print()


# LIST ==> BUAT MENDEFINISIKANNYA PAKE =>[],BUAT MEMANGGILANYA => [0], BOLEH BERULANG, NAMBAHNYA .append[x]
# SET ==> BUAT MENDEFINISKANNYA PAKE =>{}, BUAT MEMAMNGGILNYA PAKE => [0], TIDAK BOLEH BERULANG, NAMBAHNYA PAKE .add(x)
# MAP ==> BUAT MENDEFINISKANNYA PAKE =={k:v}titik ini digunakan untuk yang k untuk key memanggilnya dan v untuk value si keynya, BUAT MEMANGGILNYA =>[k] k nya digunakan sebagai
# key atau kuncinya, tidak boleh berulang atau angka atau objek yang sama, NAMBAHNYA PAKE .datasiswa["umur"] = 21

# PROJECT

siswa = [{"Nama": "Gentha Ardaana", 
          "nis" : 2021329100, 
          "Alamat" : ("Cibadak","Sukabumi"), 
          "tgl" : (28,1,2005), 
          "Kelas": (11, True, 3)},
         {"Nama" : "Juki", 
          "nis" : 202123123, 
          "Alamat" : ("Cicurug","Bandung"), 
          "tgl" : (12,9,1992), 
          "Kelas" : (10, False, 5)},
         {"Nama" : "JIJI", 
          "nis" : 202121129, 
          "Alamat" : ("Jampang","Jakarta"), 
          "tgl" : (11, 4, 2001), 
          "Kelas" : (12,True,6)}]
namaBulan = ["Januari", "Febuari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
for i in range (len(siswa)):
      dataSiswa = siswa[i]
      print("=================================================")
      print("NAMA", dataSiswa["Nama"],sep="\t\t: ")
      print("NIS", dataSiswa["nis"], sep="\t\t: ")
      kec, kab = dataSiswa["Alamat"]
      print("Alamat", kec + "- " +kab, sep="\t\t: ")
      tanggal, bulan, tahun = dataSiswa["tgl"]
      print("TANGGAL LAHIR", str(tanggal) + " " + namaBulan[bulan-1] + " " + str(tahun), sep="\t: ")
      grade,jurusan,grup = dataSiswa["Kelas"]
      print("KELAS", str(grade) + " " + ("IPA" if (jurusan) else "IPS") + " " + str(grup), sep = "\t\t: ")
      dataSiswa["umur"] = 2022 - tahun
      print("UMUR", dataSiswa["umur"], sep="\t\t: ")















