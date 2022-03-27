# Input   : berupa kumpulan angka sebanyak n (berbentuk String)
# Output  : reverse nilai dari input tersebut
# Contoh Input  : 1 2 3 4 5 6 7 8 9 0
# Contoh Output : 0 9 8 7 6 5 4 3 2 1
data = list(map(int, input().split()))
# # CARA 1 - Menggunakan looping
hasil1 = []
for i in range(len(data)):
  hasil1.append(data[len(data) - 1 - i])
print(hasil1)

# CARA 2 - Menggunakan looping dalam satu baris
print([data[len(data) - 1 - j] for j in range(len(data))])

# CARA 3 (BEST) - Menggunakan pemanggilan langsung pada array
print(data[::-1]) 
# Layaknya range(x,y,z), array juga dapat dipanggil demikian
# Jika [n:] maka array ditampilkan dari n sampai anggota terakhir, seperti range(n)
# Jika [n:m] maka array ditampilkan dari n sampai m, seperti range(n,m)
# Jika [:m] maka array ditampilkan dari anggota pertama sampai terakhir, seperti range(0, m)
# Jika [0:10:2] maka array ditampilkan dari anggota ke 0, sampai anggota ke 9 (<10) dengan langkah sebanyak 2 indeks (loncat dua) seperti range(0, 10, 2)
# Jika [::5] maka array ditampilkan dari anggota paling awal, sampai akhir dengan langkah sebanyak 5 range(0, len(arr), 5)
# Jika [::-1] maka array ditampilkan dari anggota pertama sampai terakhir dengan step -1 (turun), seperti range(len(arr) - 1, -1, -1)