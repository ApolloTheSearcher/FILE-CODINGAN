tahun = int(input("Masukan Angka tahun :"))
# cek angka tahun kabisat

if tahun % 400 == 0 or not (tahun % 100 == 0 or tahun % 4 != 0):
    kabisat= f"Tahun {tahun} ini kabisat"
else:
    kabisat = f"Tahun {tahun} ini bukan kabisat"

print (kabisat)


# cek angka ganjil genap
# if angka % 2 == 0:
#     print(f"Angka {angka} ini adalah genap")
# else:
#     print(f"Angka {angka} ini adalah ganjil")
# print("Program selesai")

# cek angka positif, negatif, nol
# if angka > 0:
#     print(f"angka {angka} ini adalah bilangan positif")
# elif angka == 0:
#     print(f"angka {angka} ini adalah bilangan nol")
# else:
#     print(f"angka {angka} ini adalah bilangan negatif")
# print("Program Selesai")