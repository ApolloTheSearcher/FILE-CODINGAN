# Input   : berupa kumpulan angka sebanyak n (berbentuk String)
# Output  : pindahkan sebuah angka pertama menjadi berada di posisi akhir list
# Contoh Input  : 1 2 3 4 5 6 7 8 9 0
# Contoh Output : 2 3 4 5 6 7 8 9 0 1
data = list(map(int, input().split()))

# CARA 1 - Menggunakan looping dengan membuat array baru
hasil1 = []
for i in range(1, len(data)):
  hasil1.append(data[i])
hasil1.append(data[0])
print(hasil1)

# CARA 2 - dengan menggunakan pemanggilan sebagian array
hasil2 = data[1:]
hasil2.append(data[0])
print(hasil2)

# CARA 3 (BEST) - Pemanggilan array langsung dilakukan concatenance untuk array
print(data[1:] + [data[0]])
# data[1:] memanggil seluruh anggota array mulai dari index 1, sehingga anggota pertamanya tidak masuk
# data[0] adalah memanggil data pertama
# [data[0]] adalah merubah nilai menjadi bentuk List (array) contoh: data[0] = 1, maka [data[0]] = [1] (berbentuk array/List)
# kita bisa menggabungkan array mis: [1, 2] + [3, 4] = [1, 2, 3, 4]
# data[1:] + [data[0]]