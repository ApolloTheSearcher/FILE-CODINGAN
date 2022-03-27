# While
# Digunakan untuk meneksekusi statement selama kondisi yang diberikan terpenuhi (True).
# Kondisi yang diberikan terpenuhi (True). Kondisi dapat berupa expression apapun,
# dan harap diingat bahwa True di Python termasuk semua nilai non-zero.
# Saat kondisi menjadi False, program akan melanjutkan ke baris setelah blok statement.
'''
penulisan:
while (condition):
    statement
    proses
statemen dan proses bebas ya guys ya bisa salah satu atau bisa keduanya
kaya nulis if statement kalau while itu
'''
# Contoh program hitungan:
count = 0
while (count < 7):
    print(f"Count: {count}")
    count = count + 1
'''
kode di atas akan proses jika setiap condition pada while bernilai true
dan akan berakhir jika count itu bernilai false
nah jika kita tidak memberi suatu proses atau statement maka akan infite looping
karena while mungkin bersifat infinite looping saat kondisi tidak pernah bernilai False.
Berikut dibawah adalah contoh program infite looping
'''
# var = 1
# while var == 1:
#     num = input("Masukan Angka: ")
#     print(f"Angka yang anda masukan adalah: {num}")
# while True:
#     num = input("Masukan Angka: ")
#     print(f"Angka yang anda masukan adalah: {num}")
# Nah jika kita mendapat kan sebuah yang tidak dapat berhenti jangan panik ya wkwk!
# kita dapat menghentikan dengan paksa yaitu dengan menggunakan CTRL atau CMD + C dia akan berhenti dan
# keluar dari program
# atau kita juga dapat menggunakan statement break untuk menghentikan paksa bila program itu memang true dan terjadi
# Contoh di bawah:
angka = 1 
while (angka <= 10):
    print(f"Angka: {angka}")
    angka += 1
    if (angka == 5):
        break
# program ini akan berhenti dengan paksa jika angka itu bernilai 5
# program ini juga masuk gabungan menggunakan if statement dan ada statement break
# Selain itu kita juga dapat menyingkat penulsan blok statement While jika statement 
# Anda cukup terwakili oleh satu baris.
# while (variable):statement => penulisannya.
# Contoh di bawah:
var1 = 0
while(var1): print(var1)


