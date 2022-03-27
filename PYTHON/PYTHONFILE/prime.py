import time

max = 1000# Ubah angka ini untuk menentukan nilai maksimum garis bilangan primanya
show = True # Ubah True atau false untuk melihat hasil dari bilangan primanya

# print("Nilai Maksimum :", max)

# for i in range(40): print("-", end="")
# print("\nMetode biasa\n")

# total = 0
# isPrime = 0
# notPrime = 2
# waktu = time.process_time()
# hasil = ""
# for i in range(2, max):
#     total += 1
#     prime = True
#     for k in range(2, i):
#         total += 1
#         if(i % k == 0 and k != 1):
#             prime = False
#             # Menggunakan break untuk menghentikan proses sesaat
#             # jika bilangan bukan prima
#             break
#     if(prime):
#         isPrime += 1
#         hasil += str(i) + ", "
#     else:
#         notPrime += 1

# if(show) : print(hasil)
# print("\nJumlah prima\t\t:", isPrime)
# print("Jumlah bukan prima\t:", notPrime)
# print("Jumlah perulangan\t:", total)
# print("Waktu proses\t\t:", (time.process_time() - waktu) * 1000, "ms")
 
# for i in range(40): print("-", end="")       
# print("\nMetode garis bilangan dibagi dua\n")

# total = 0
# isPrime = 0
# notPrime = 2
# waktu = time.process_time()
# hasil = ""
# for i in range(2, max):
#     total += 1
#     prime = True
#     for k in range(2, int(i/2) + 1):
#         # Mengurangi banyak proses dengan memotong proses menjadi dua
#         total += 1
#         if(i % k == 0 and k != 1):
#             prime = False
#             break
#     if(prime):
#         hasil += str(i) + ", "
#         isPrime += 1
#     else:
#         notPrime += 1

# if(show) : print(hasil)
# print("\nJumlah prima\t\t:", isPrime)
# print("Jumlah bukan prima\t:", notPrime)
# print("Jumlah perulangan\t:", total)
# print("Waktu proses\t\t:", (time.process_time() - waktu) * 1000, "ms")

# for i in range(40): print("-", end="")


print("\nMetode Sieve of Erathostenes\n")
# Referensi : https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
total = 0
isPrime = 0
notPrime = 2
#waktu = time.process_time()
hasil = ""
i = {} # Menggunakan dict sebagai himpunan angka
for n in range(2, max):
    i[n] = True
    total += 1
for k in range(2, len(i) + 2):
    total += 1
    if(i[k]):
        val = k
        isPrime += 1
        hasil += str(val) + ", "
    else:
        notPrime += 1
        continue
    for n in range(val*2, len(i) + 2, val):
        i[n] = False
        total += 1
        
if(show) : print(hasil)       
print("\nJumlah prima\t\t:", isPrime)
print("Jumlah bukan prima\t:", notPrime)
print("Jumlah perulangan\t:", total)
#print("Waktu proses\t\t:", (time.process_time() - waktu) * 1000, "ms")

