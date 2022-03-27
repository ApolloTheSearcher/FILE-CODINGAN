#himpunanAngka = [2,4,6,4,1,20] namanya LIST

#himpunanNama = ["Ananda", "Sasan", "Dewi", "Atha", "Jaa", "Shiva"]

#print(himpunanAngka [2])
#print(himpunanNama [0])

#print(himpunanAngka [-3])
#print(himpunanAngka [0 : 2])
#print(himpunanNama [ : -1])

#print (himpunanAngka[2:-2])

#for a in range (len(himpunanAngka) -1, -1, -1):
#   print (himpunanAngka [a])
   
#for a in range (0,len(himpunanAngka),2) :
 #  print (himpunanAngka [a])
 #List nambahinnya pke append(x)

#s = {1,2,1,3,4,3} namanya SET, gk akan berulang
#nambahin set pake add(x
#jenis array selanjutnya adalah TUPLE
#bentuk tuple ==> tanggalLahir = (21,1,2005)
#tanggal, bulan, tahun = tanggalLahir

#satu lagi array namanya MAP
# m = {1:6, 2:7, 3:10, 4:17}
siswa = [{
	      "Nama" : "Ananda Septiani",
       "NIS" : 202110145,
       "Alamat" : ("Caringin", "Sukabumi"),
       "Tanggal Lahir" : (21,1,2005),
       "Kelas" : (11, True, 5)},
       {
	      "Nama" : "Atha",
       "NIS" : 202110565,
       "Alamat" : ("Cicurug", "Sukabumi"),
       "Tanggal Lahir" : (17,1,1970),
       "Kelas" : (7, False, 5)},
       {
	      "Nama" : "Sandrina",
       "NIS" : 2021256745,
       "Alamat" : ("Cisaat", "Sukabumi"),
       "Tanggal Lahir" : (21,1,1985),
       "Kelas" : (1, True, 8)}]
       

namaBulan = ["Januari",
             "Februari",
             "Maret",
             "April",
             "Mei",
             "Juni",
             "Juli",
             "Agustus",
             "September",
             "Oktober",
             "November",
             "Desember"]

for i in range (len(siswa)):
    dataSiswa = siswa[i]
    print("Nama", dataSiswa["Nama"], sep="\t\t :")
    print("NIS", dataSiswa["NIS"], sep="\t\t :")
    kec, kab = dataSiswa["Alamat"]
    print("Alamat", kec + ", " + kab, sep="\t\t :")
    tanggal, bulan, tahun = dataSiswa["Tanggal Lahir"]
    print("Tanggal Lahir", (str(tanggal) + " " + 
	                      namaBulan[bulan - 1] + " " + 
	                      str(tahun)), sep =" \t :") 

    grade, group, rombel = dataSiswa["Kelas"]
    print("Kelas", str(grade) + " " + ("IPA" if (group) else "IPS") + " " + str(rombel), sep="\t\t :")
    dataSiswa["Umur"] = 2022 - tahun
    print("Umur", str(dataSiswa["Umur"]), sep=" \t\t :",)
    print ()
