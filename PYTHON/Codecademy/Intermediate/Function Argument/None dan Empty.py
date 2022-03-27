# Python a GOTCHA
def dataNilaiSiswa(name, age, grades=[]):
    return{
        "Nama" : name,
        "Umur" : age,  # Dict dari si fungsi dataNilaiSiswa
        'Grade' : grades
    }
# Kita panggil
dataNilaiSiswa("Rizki", 20)
dataNilaiSiswa("Paijo", 17)
# Nah kalau gini kita bisa jadikan kalau misalnya si score tidak di masukan atau mau di masukan telat kita buat
# Semacam fungsi default supaya nanti bisa ditambahkan
# Contoh:
def tambahNilaiSiswa(nama, nilai):
    nama['Grade'].append(nilai)
    print(nama['Grade'])
# Kita panggil
tambahNilaiSiswa(dataNilaiSiswa("Rizki", 20), 90)  # Kita masukan nilai 90
tambahNilaiSiswa(dataNilaiSiswa("Paijo", 20), 70) # Kita bisa gunakan ini atau bisa juga menyimpan nilai fungsi dataNilaiSiswa ke dalam variable bebas
# Contoh:
Rizki = dataNilaiSiswa("Rizki", 20)
tambahNilaiSiswa(Rizki, 90)
# Nah inii yang bisa kita sebuah sebagai PYTHON GOTCHA!!
# Outputnya: [90] [90,70] [90,70,90] => diakan bertambah data didalam listnya setiap kita menambahkan data kedalamnya
# Tetapi kan yang kita mau itu adalah di akan berbeda list jika kita menambahkan nama yang berbeda pula
# Kita bisa menggunakan NoneWorkaround jika ingin nilai yang berbeda ketika namanya yang dimasukan berbeda
# Tetapi kita jika ingin tetap menggunakan empty list dengan nilai yang benar benar tidak boleh di isi di awal
# kita bisa menggunakannya dengan cara None Workaround
'''
kita dapat menggunakan None sebagai nilai khusus untuk menunjukkan bahwa kita tidak menerima apa pun.
Setelah kami memeriksa apakah argumen diberikan, kami dapat membuat instance daftar baru jika tidak.
Berikut adalah seperti apa solusi untuk program kami dari sebelumnya:
'''
def dataNilaiSiswa1(name, age, grades=None):
    if grades is None:
        grades = []
    return{
        "Nama" : name,
        "Umur" : age,  # Dict dari si fungsi dataNilaiSiswa
        'Grade' : grades
    }
def tambahNilaiSiswaLain(nama, nilai):
    nama['Grade'].append(nilai)
    print(nama['Grade'])
# Kita panggil dataNilaiSiswa1 akan kita masukan kedalam variable
Budi = dataNilaiSiswa1("Budi", 20)
tambahNilaiSiswaLain(Budi, 90)
Laskar = dataNilaiSiswa1("Laskar", 20)
tambahNilaiSiswaLain(Laskar, 70)
# Outputnya:
# [90]
# [70] => karena kita menggunakan None Workaround seperti yang kita inginkan outputnya
