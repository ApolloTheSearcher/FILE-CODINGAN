# Branching merupakan sebuah cara untk melakukan percabangan pada sebuah logika/algoritma program
# Contohnya adalah jika kita memenuhi kondisi A, maka kita menjalankan program A,
# jika tidak, maka program lain akan di jalankan.
# Contoh kasus lain pada dunia nyata misalkan adalah jika sedang turun hujan,
# kita akan membawa payung.
# Hal ini diimplementasikan dengan menggunakan percabangan "Jika" atau dalam bahasa inggris
# disebut sebagai if.
# Terdapat tiga jenis if untuk menunjukkan percabangan
# dimana pertanyaan pada if di anggap sebagai gerbang menuju bagian program lain.
# jika perntanyaan if terpenuhi, maka blok program di dalam if akan di jalankan
# jika tidak, maka blok program di dalam if akan dilewat.

if True :
    print("Hello")

print("Selesai")

# dari contoh di atas, cara penulisan if adalah if, kemudian diikuti oleh data bool atau logika
# yang menunjukkan benar atau salah (True, False). jika if memiliki hasil pengujian True,
# maka bagian program di dalam if tersebut akan di jalankan yaitu baris ke 14,
# kemudian akan keluar dari blok if tersebut lanjut kedalam baris 16.

if False:
    print("Hello")
print("Selesai")

# jika data yang masuk kedalam if bernilai False, maka blok program dalam if, dalam hal ini
# adalah baris ke 14, atau 24 tidak akan di eksekusi oleh komputer sehingga dari baris 23
# akan langsung loncat ke 25.

a = 10
b = 20

if (a == b): # False
    print("A sama dengan B") # Di lewat
    
# pengujian if juga dapat dilakukan seperti contoh di atas,
# yang penting hasil dari proses yang dilakukan berupa bolean, sehingga
# dapat menggunakan proses logika perbandingan dan opeasi logika dalam baris yang sama dengan
# if

x = 10 % b < 5 and a == b
if x: # False
    print ("Sesuai dengan kaidah")
    x = 20
    print("X di ganti nilainya")
    
print("Selesai")    

# Data input untuk if juga dapat di ambil dari nilai di dalam variabel, contohnya adalah
# bagian if di atas yang mengambil data boolean dari variabel x
# blok program dapat di tulis sebanyak-banyaknya asalkan indentasi nya sama
# indentasi merupakan jarak antara bagian program dengan bagian program lainnya.
# setelah gerbang logika seperti if ditulis, maka WAJIB memiliki indentasi di bawahnya
# indentasi biasanya menggunakan Tab untuk memberi jarak pada blok program,
# dapat juga menggunakan spasi sebelum sintaks program tersebut
# Indentasi tidak dapat dilakukan jika blok program tidak memiliki gerbang masuk
# Dalam konteks ini contoh gerbang masuknya adalah pertanyaan pada if

# Contoh yang tidak benar
# if a == b
#   print("Hello")
# contoh di atas salah karena pada akhir if tidak memakai titik dua

# if a == b:
# print(a+b)
# contoh di atas salah karena tidak ada indentasi setelah gerbang if

# print(a)
# print(b)
#   print("Hello")
# print(a + b)
# contoh di atas salah karena terdapat blok program yang memiliki indentasi
# tetapi tidak memiliki gerbang

# print(a)
# if (a < b):
#   print(a + b)
# print("Hello")
#   print(b - a)
# contoh di atas salah karena blok program hanya benar ketika masuk pada
# gerbang baris 77 dan bloknya pada 78.
# sementara pada baris 80 di anggap bahwa indentasi yang di bentuk
# membuat baris tersebut menjadi blok baru tanpa adanya gerbang.

if True:
    pass

print("Selesai")

# untuk menulis blok if tanpa blok program internal, kita dapat menggunakan perintah pass
# untuk melewati blok program if tersebut.

if a < b:
    print("Hello")
    if(True):
        print("Masuk")
    print("If bagian A")
print("Selesai")

# bagian blok program juga dapat dibentuk secara nested, atau beranak pinak atau
# blok program didalam blok program, yang terpenting adalah menggunakan kaidah yang sama.

if a + b < 100:
    if(a - b) > 2:
        print("True")
    if(a - b) <= 2:
        print("False")
    print("Merupakan angka")
    
# di atas merupakan contoh lain dari percabangan, yang mana membawa kita pada jenis selanjutnya
# dapat di pahami bahwa pada baris 105 saat a = 10, b = 20 maka jika lebih dari 2 akan
# menghasilkan False, kemudian logika jika pada 107 akan bernilai True. hal ini
# menjadi logika yang meneria kondisi selain dari kondisi pada baris 105. sehingga
# untuk memudahkan penulisan, kita dapat menggunakan else, sebagai bagian program
# pada percabangan untuk menerima pengujian data bernilai False.

if a + b < 100:
    if(a - b) > 2:
        print("True")
    else:
        print("False")
    print("Merupakan angka")
    
# bagian program else, harus di awali oleh induk if, sehingga bagian if akan selalu menerima kondisi True
# sementara bagian else akan selalu menerima kondisi False.

if a % 2 == 1:
    print("Angka Ganjil")
else:
    print("Angka Genap")
    
# di atas merupakan contoh lain penulisan if-else.
# percabangan digunakan secara bebas dan tidak ada kaidahnya,
# yang penting logika atau output yang di inginkan penulis program sesuai harapan.

if a > 0:
    print("Angka positif")
elif a < 0:
    print("Angka negatif")
else:
    print("Angka Nol")

# contoh di atas merupakan jenis percabangan if-elif-else
# elif di tulis setelah if dan sebelum else.
# elif dapat di tulis sebanyak mungkin untuk menerima kondisi lain, jika if atau elif
# di atasnya terlah bernilai false
# tidak ada kewajiban menabahkan else jika ingin menggunakan elif.
# elif akan menjalankan blok program di dalamnya ketika bernilai True, jika tidak
# maka akan melanjutkannya pada bagian program di luarnya

if a == 1:
    print("Satu")
elif a == 2:
    print("Dua")
elif a == 3:
    print("Tiga")
elif a == 4:
    print("Empat")

# perlu di ingat, bahwa bagian elif harus selalu memiliki if, tetapi else
# tidak selalu harus, tergantung kondisinya, apakah kita menginginkan
# nilai False nya memiliki proses atau tidak.
# program di atas akan berjalan jika salah satu kondisinya sesuai, jika kondisinya tidak sesuai maka
# program akan di lewat.

x = 10

if(a < 10): # False
    print("Kurang dari 10")
elif a < 20: # True
    print("Kurang dari 20")
elif a < 30: # Di lewat, karena sudah True dan masuk kedalam blok 172
    print("Kurang dari 30")
else : # Di lewat, karena sudah True dan masuk ke dalam blok 172
    print("Lainnya")
    
print("Selesai") # di jalankan karena diluar keluarga if di atas

# bagian di atas merupakan contoh if-elif-else lainnya
# pada bagian tersebut, hanya di jalankan bagian 172, karena
# gerbang elif pada 171 terpenuhi dan menghasilkan True.
# walaupun gerbang 173 dapat menghasilkan True juga, tetapi hal tersebut
# tidak di lakukan, yaitu langsung di lewat (di skip), keluar dari
# keluarga if tersebut menuju bagian 178.