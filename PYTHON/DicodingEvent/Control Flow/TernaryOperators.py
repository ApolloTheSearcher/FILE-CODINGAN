# Perbandingan IF dengan Tenary Operator 
'''
if (condition):
    condition_if_true
else:
    condition_if_false
Sedangkan jika ternary itu:
condition_if_true if,condition else condition_if_false
========================================================
Selain itu Ternary Operator juga melibatkan tuples.
if (condition):
    (condition_if_true)
else:
    (condition_if_false)
Sedangkan bentuk ternary_tuples itu:
(condition_if_false),(condition_if_true)[condition]
pada tuple ini dimanfaatkan nilai [0] sebagai false, dan [1] sebagai true
===========================================================
'''
# Contoh penggunaan ternary operator pada variable biasa
bilangan = int(input("Masukkan bilangan: "))
menentukanBilangan = f"Bilangan {bilangan} adalah ganjil" if bilangan % 2 == 1 else f"Bilangan {bilangan} adalah genap"
print(menentukanBilangan)
# Outputnya:
# misalkan yang dimasukan itu angka 11
# Bilangan 11 adalah ganjil

# Contoh penggunaan ternary operator melibatkan tuples
bilangan2 = int(input("Masukkan bilangan2: "))
menentukanBilangan2 = (f"Bilangan {bilangan2} adalah genap"), (f"Bilangan {bilangan2} adalah ganjil")[bilangan % 2 == 1]
print(menentukanBilangan2)
# Outputnya jika tuple itu:
# ('Bilangan 20 adalah genap', 'B')
# nah pada output ini dimana terdapat 2 itu adalah index [0] itu adalah condistion_if_true,
# sedangkan pada index [1] itu dapat karena yang nilai kita masukan 2 nah di hitung sebagai alfabet, huruf ke-2 alfabet itu kan 2
# Jadi hasilnya juga 2

# ShortHand Ternary
# digunakan untuk mungkin membantu anda untuk memeriksa kode/hasil dari sebuah fungsi dan
# memastikan outputnya tidak menyebabkan error
# (atau minimal memberikan informasi relevan saat error)
# contoh kode:
hasil = None
pesan = hasil or "Tidak ada data"
print(pesan)
# Outputnya:
# Tidak ada data bukan True atau False karena pada kasus ini dimana None itu memang tidak ada hasilnya
# variable yang kosong tidak diisi apa apa


