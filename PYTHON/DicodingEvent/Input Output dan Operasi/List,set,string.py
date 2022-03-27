# len()
# digunakan untuk menghitung banyaknya karakter dalam sebuah string.
# contoh:
contoh_list = [1,2,3,3,3,3,2,2,1,2,2,5,6,5,3,6,]
print(contoh_list)
print(len(contoh_list))
# Outputnya :
# [1, 2, 3, 3, 3, 3, 2, 2, 1, 2, 2, 5, 6, 5, 3, 6]
# 16
contoh_string = "Belajar Python"
print(contoh_string)
print(len(contoh_string))
# Outputnya :
# Belajar Python
# 14

# min() dan max()
# min() dan max() digunakan untuk mencari nilai terkecil dan terbesar dari sebuah list atau sebuah string.
# contoh:
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

# Count
# untuk mengetahui berapa kali suatu objek muncul dalam list, anda dapat menggunakan fungsi count()
# contoh:
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

# in dan not in
# in itu True jika objek yang dicari ada dalam list, dan False jika tidak ada.
# not in itu True jika objek yang dicari tidak ada dalam list, dan False jika ada.
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat) # True
print('tidak' in kalimat) # False

# memberikan nilai untuk variable
# bisa dari list atau tuple nilainya dimasukan kedalam variable.
# contoh:
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]
# atau
data = ['shirt', 'white', 'L']
apparel,color,size = data
# bentuk tuple
data = ('shirt', 'white', 'L')
apprel,color,size = data
# Ingat harus sama jumlah variable dengan jumlah nilai yang ada didalam list atau tuple
# jika tidak sama, maka akan error

# Sort sort()
# sort() digunakan untuk mengurutkan list atau tuple secara ascending.
# tetapi tidak bisa jika didalam list atau tuple terdapat angka dan string sekaligus
