pengecekaan = True
pengecekaan = False
print(pengecekaan)

angka1 = 100
angka2 = 200
hasil = angka1 < angka2

print("Hasil pengujian :" + str(hasil))
# ini disebut operasi konket karena penambahan pada kalimat

# Metode menggabungkan kata
# 1. Concatenation (penggabungan kata)
#    kata = kata1 + str(angka 1) + "Literall"
# 2. Input Parameter print
#    print(kata1,angka1)   
# 3. Literal Formating (format)
#    kata = f"Literall {angka1}"
# 4. Method Formatting (format)
#    kata = "{} Literall {}".format(kata1,angka1)


# Input
angka1 = int(input("Masukkan angka 1: "))
angka2 = int(input("Masukan angka 2: "))
hasil = angka1 < angka2
print("Hasil penjumlahan: ", hasil)

# IF STATEMENT
if hasil:
    print("angka 1 tidak sama dengan angka 2")
else:
    print("angka 1 sama dengan angka 2")

# ELSE STATEMENT
# else harus sesudah if ya karena control flow itu di awali dengan if
