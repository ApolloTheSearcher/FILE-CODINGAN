# For
# For tidak hanya untuk perulangan dengan jumlah finite(terbatas), melainakan lebih ke fungsi yang dapat melakukan perulangan pada
# pada setiap jenis variable berupa kumpulan atau urutan.
# Variable yang dimaksud bisa berupa list, string aataupun range.
# Contoh:
# for huruf in 'Python':
#     print(f"Huruf {huruf}")
'''
penulisan:
for (variable) in (sequence):
    statement
    proses
atau jika menggunakan range
for (variable) in range(start, stop, step):
    statement
    proses
    
untuk proses dan statement bebas ya gk mesti kaya gitu ya bisa salah satu atau bisa keduany
bisa gk usah di isi juga bisa
'''

# Contoh perulangan berupa list. (Toko Bunga Program Sederhana)
# tokoBunga = ["Mawar", "Melati", "Anggrek"]
# for bunga in tokoBunga:
#     print(f"Bunga yang ada ditoko itu ada Bunga {bunga}")
# # Contoh dibawah jika menggunakan range
# hitungJumlah = []
# for berapaBunga in range (len(tokoBunga)):
# # Contoh di atas adalah penggunaan range()
#     hitungJumlah.append(berapaBunga)

# print(f"Jumlah Bunga yang ada di Toko Bunga Bu LILA : {len(hitungJumlah)} Bunga")
# Cuma kalo range itu menghitung indexnya sebagai perulangan
# Fungsi range() mengembalikan urutan angka, dimulai dari 0 secara default, dan bertambah 1 (secara default), dan berakhir pada angka
# yang ditentukan.
# Selain itu range() terdapat bagian atau parameternya/
# range(awal, akhir, step/Langkah)
# Nah perulang itu digunakan seperti itu jadi dia bakal kembali keatas sampai batas nya sudah melebih
# Jika ingin menghitung ada berapa bunga yang ada didalam tokoBunga tidak usah memakai.
# Selain itu for juga dapat digunakan bersarang
# Contohnya itu ada looping didalam looping
# Contoh program looping didalam looping menggunakan for range() dengan membuat program setengah segitiga.
# for i in range (10):
#     for j in range (10 - i):
#         print(j, end="")
#     print()
'''
disini kita menggunakan for range() untuk menghitung setengah segitiga
nah setengah segitiga terjadi karena pada looping di dalam looping memasukan range yang dimana itu 10 berati program bacanya dari atas
Contoh lain
'''
n = 10
for t in range (n + 1):
    for l in range (n * 2):
        karakter = " "
        if l >= t and l < (n * 2)- t - 1:
            karakter = l - t
        print(karakter, end = " ")     
    print()
