kata = "Hello"
angka = 20
# Metode menggabungkan kata
# 1. Concatenation (penggabungan kata)
#    kata = kata1 + str(angka 1) + "Literall"
hasilConcat = kata + " : " + str(angka)
print(hasilConcat) 
# 2. Input Parameter print
#    print(kata1,angka1)
print(kata,angka)   
# 3. Method Formatting (format)
#    a. anonymous Format
hasilAnomForm = "{} {}".format(kata,angka)
print(hasilAnomForm)
# untuk anomnya kita tidak bisa menggunakan banyak isinya
#    b. indexed Format
hasilIndexForm ="{1} {0}".format(kata,angka)
print(hasilIndexForm)
# untuk indexed harus dimulai dengan angka 0
#    c. named Format
hasilNameForm ="{angka} {kata}".format(angka=angka,kata=kata)
print(hasilNameForm)
# untuk named itu kaya ada variable baru untuk mem verifikasinya kembali.
# 34 Literal Formating (format)
#    kata = f"Literall {angka1}"
hasilLitteralFormat = f"{kata} {angka}"
print(hasilLitteralFormat)




