# Output
# Biasanya kita menggunakan fungsi print() adalah cara output langsung ke konsol/layar. 
# print("Hello World!")
# untuk menampilkan text(string), bisa menggunakan mekanisme string format. Misalnya yang pertama:
print("Hai {}!".format("Dicoding"))
# cara yang kedua mirip dengan sintaks C/C++, yakni menggunakan operator "%" yang ditambahkan
# dengan "argument specifiers", misalnya "%s" and "%d". Contohnya saat kita ingin menambakan nama kita pada string Hello:
# %s digunakan untuk menambahkan string
# %d digunakan untuk menambahkan integer
# Contoh:
nama = "Dicoding"
print("Hello %s!" % nama)
# Outputnya : Hello Dicoding!
# Contoh menambahkan string dan interger:
nama = "Dicoding"
umur = 12
print("Umur %s adalah #d tahun." % (nama,umur))
# Outputnya : Umur Dicoding adalah 12 tahun.
# INPUT
a = int(input("Masukkan angka pertama: "))
print(a)

# Command-line Arguments
# Python memungkinkan anda untuk membuat sebuah"skrip" berupa deretan kode program kemudian disimpan dalam sebuah berkas dengan nama akhiran.py

#contoh:
import sys
print("Jumlah arguement:", len(sys.argv), "arguments")
print("Argument yang diberikan:", str(sys.argv))
print(sys.argv[len(sys.argv)-1])

# Untuk len itu tidak bisa bila seperti contoh dibawah:
x = 546
print(len(x))
# Outputnya : TypeError: object of type 'int' has no len() akan error
# bila kita print kan x, maka akan error







