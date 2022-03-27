# IF (jika)
bolaku = 10
if bolaku:
    print('Bolaku adalah 10')
    print(bolaku)
# atau bisa dipersingkat menjadi
if bolaku:print("Bolaku adalah 10"),print(bolaku)
#ELSE (TIDAK)
# Statement Else dapat dikombinasikan dengan IF Statement, sebagai jalan keluar
# saat kondisi/hasil evaluasi bernilai False.
#Contoh menghitung tinggi badan
tinggi_badan = int(input("Masukkan tinggi badan anda: "))
if tinggi_badan>=160:
    print("Tinggi badan anda terlalu tinggi")
else:
    print("Tinggi badan anda terlalu rendah")
# atau contoh mencari bilangan ganjil atau genap
bilangan = int(input("Masukkan bilangan: "))
if bilangan % 2 == 0:
    print("Bilangan {} adalah genap".format(bilangan)) # => anonymous format
    print("Bilangan {1} adalah ganjil".format(bilangan)) # => index Format
    print("Bilangan{bilangan} adalah ganjil".format(bilangan=bilangan)) # => named Format
    print(f"Bilangan {bilangan} adalah genap") # => Literal Format
else:
    print("Bilangan {} adalah ganjil".format(bilangan)) # => anonymous format
    print("Bilangan {1} adalah ganjil".format(bilangan)) # => index Format
    print("Bilangan{bilangan} adalah ganjil".format(bilangan=bilangan)) # => named Format
    print(f"Bilangan {bilangan} adalah ganjil") # => Literal Format

    
# Elif (jika kondisi lain) Alternatif untuk switch case dan if bertingkat
# Sebuah IF Statement dapat diikuti satu atau lebih statement elif (opsional & tidak dibatasi)
# Contoh Impelementasikan kedalam kasus penilaian tugas siswa
nilai = int(input("Masukkan nilai tugas anda: "))
if nilai>80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai>70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai>60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")