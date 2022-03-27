#Number terdiri menjadi 3 : int,float,complex
#untuk complex contoh:
c = 1+2j
print(c,"Bertipe bilangan kompleks?", isinstance(c,complex))
# outputnya dari atas yaitu (1+2j) Bertipe bilangan kompleks? True
# untuk bilangan kompleks(complex) dituliskan dalam formulasi x + yj, yakni bagian x adalah bilangan real dan y adalah bilangan imajiner

#String 
#String yang lebih dari 1 baris dapat ditandai dengan tiga petik tunggal atau ganda " atau """
# Contoh:
s = '''Ini adalah string yang
memiliki baris pertama
dan selanjutnya baris kedua '''
print(s)
#outputnya : Ini adalah string yang
#            memiliki baris pertama
#            dan selanjutnya baris kedua

# List
# Contoh:
x = [5,10,15,20,25,30,35,40]
print(x[0])
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])
# X[5] artinya mengambil nilai dari index ke 5
# x[0] artinya mengambil elemen paling awal dengan index 0 dari List x
# x[-1] artinya mengambil elemen paling akhir dengan index -1 dari List x
# x[3:5] artinya mengambil elemen dari index 3 hingga sebelum index 5 (tidak temasuk elemen dengan index 5, dalam hal ini hanya indec 3-4)
# x[:5] artinya mengambil elemen dari index 0 hingga sebelum index 5 (tidak termasuk elemen dengan index 5, dalam hal ini hanya indec 0-4)
# x[-3:] artinya mengambil elemen dari anggota elemen List x mulai index ke-3 dari belakang hingga paling belakang.
# x[1:7:2] artinya membuat list dari anggota elemen List x dengan index 1 hingga sebelum index 7, dengan "step" 2 (dalam hal ini hanya index 1,3,5).
# Outputnya :
# 5
# 30
# 40
# [20,25]
# [5,10,15,20,25]
# [30,35,40]
# [10,20,30]

# Tuple (tidak bisa di ganti nilainya)
# Tuple bersifat sekali tulis, dan dapat dieksekusi lebih cepat.

# Set
# Set adalah kumpulan item bersifat unik dan tanpa urutan *unordered collection).
# Didefinisikan dengan kurawal dan elemennya dipisahkan dengan koma.
# Contoh: 
a = {1,2,2,3,3,3}
print(a)
print(a[1]) # karena bersifat unordered, maka kita tidak bisa mengambil sebagian data/elemen datanya menggunakan proses slicing.

# Dictionary
# Dictionary adalah kumpulan item yang memiliki key dan value. yang bersifat tidak berurutan.
# dapat digunakan untuk menyimpan data kecil hingga besar.
# untuk mengakses datanya, kita harus mengetahui keynya (kuncinya).
