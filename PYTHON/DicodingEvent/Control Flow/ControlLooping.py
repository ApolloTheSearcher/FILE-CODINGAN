# Kontrol Perulangan
# Break
# Break disini digunakan untuk menghentikan perulangan dan kemudian keluar dari perulangan hanya dapat dipakai saat perulangan ya.
# Jika memiliki perulangan bertingkat, break akan menghentikan perulangan sesuai dengan tingkatan atau diperulangan mana ia berada.
# Namun jika ia diletakkan di perulangan dengan kedalaman kedua misalnya, hanya perulangan itu saja yang berhenti, tidak dengan perulangan utama.
# Contoh perulangan dengan break
'''
for t in range (20):
    for l in range(0,10):
        if (t == 10):
            break
        else:
            print(t, )
'''
# Contoh perulangan dengan break
# for i in range (0,10):
#     for j in range (0,10):
#         if j > i:
#             print()
#             break
#         else:
#             print("*", end = " ")
#     print()
    
# Continue
'''
Pernyataan continue akan membuat iterasi saat ini berhenti, kemudian melanjutkan ke iterasi berikutnya,
mengabaikan pernyataan (statement) yang berada antara continue hingga akhir blok perulangan.
'''
# Contoh perulangan dengan continue
# for huruf in 'Gentha':
#     if huruf == 'a':
#         continue
#     print(f"Huruf saat ini {huruf}")
# Contoh mebuat perulangan dengan continue segitiga (while)
'''
jumlahBaris = 10
baris = 0
bintang = 0
while baris < jumlahBaris:
    if (bintang) >= (baris+1):
        print()
        baris += 1
        bintang = 0
        continue
    print("*", end = " ")
    bintang += 1
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, ' adalah bilangan prima')
