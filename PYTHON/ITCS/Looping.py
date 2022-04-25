# While looping
# a = 10
# while a > 0: # Jika ingin stop harus menghasilkan nilai False
#     print(a)
#     a -= 1
# print("Program selesai") # <=====

# # For looping
# # Digunakan untuk jenis type data struktur (List, dict, Tuple, Map, dll)
namaOrang = ["Budi", "Joko", "Mega", "Dedy"] 
for nama in range(len(namaOrang)):
    print("Nama : ", namaOrang[nama])
print("Selesai")

# For range Looping
# for n in range(10):
#     print(n)
# class range()
# range(awal, akhir, tahap)

# break dan continue
# a = 0
# while True:
#     a += 2
#     print("Nilai Awal")
#     if(a % 2 == 0):
#         print(a, "Nilai ini Genap")
#         continue
#     elif(a < 100):
#         break
#     else:
#         print(a, "Ganjil")
#     print("Balik lagi")

# for i in range(5):
#     print(i)
#     if i == 2: 
#         break

# Fungsi pass
# a = True
# b = 0
# while a:
#     b += 2
#     print(b, end=", ")
#     if b < 10:
#         pass
#     else:
#         a = False


# Study Case
# Kotak dengan for range looping:
# tinggi = 4
# for t in range(tinggi):
#     for l in range(tinggi):
#         print("*", end=" ")
#     print("")

# Segitiga sebelah
# tinggi = 10
# for t in range(0, tinggi):
#     for l in range(0, t + 1):
#         print("*", end="")
#     print("")

# Segitiga full
# tinggi = 10
# for t in range(tinggi):
#     for l in range(tinggi * 2):
#         karakter = ""
#         if l == (tinggi - 1) - t:
#             karakter = "/"
#         elif(tinggi * 2) - l == tinggi - t:
#             karakter = "\\"
#         else:
#             if(t == tinggi - 1):
#                 karakter = "-"
#             else:
#                 karakter = ""
#         print(karakter, sep="", end="")
#     print()
    
    