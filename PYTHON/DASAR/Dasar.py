# VARIABLE
# Penulisan variable itu ada

# Snake_Case
# Contoh:
from re import X


variable_b = "Aku Cinta Kamu"

# camelCase
# Contoh:
variableUntukAngka = 10
# nah pada penulisan ini biasanya camelCase itu menulis itu Setiap kata, kecuali yang pertama, dimulai dengan huruf kapital

# PascalCase
# Contoh:
AkuSebagaiVariable = "Aku ini Contoh Variable"
# nah pada penulisan ini sama dengan camelCase cuma yang ini huruf pertamanya menggunakan huruf kapital

# Variable bisa memuat banyak isi di dalamnya atau pun bisa 3 variable bisa sama isinya 

# Many Value to Multiple Variable
a,b,c = "orang", "Manusia", "Ketua"
"""
Nah untuk ini adalah variable dimana variable itu bisa dibuat dalam 1 shell yang sama hanya saja jangan
lupa untuk menambahkan tanda koma(,) karena tanda itu akan menandakan bagian bagian variable nya
di atas variable si a adalah orang, variable si b itu adalah Manusia, dan Variable si c itu adalah Ketua
"""
# Selain itu kita juga bisa menuliskan isi variable yang sama kedalam variable yang berbeda dengan 1 shell kerja
# Disebut:
# One Value to Multiple Variable
x=y=z = "Orange"
"""
Diatas itu adalah cara bagaimana jika kita ingin memasukan data variable yang sama kedalam sebuah variable yang berbeda-beda. jangan lupa
menambahkan tanda (=) karena supaya program bisa membaca bahwa mereka itu sama
"""
# Selain itu kita bisa menggabungkan sebuah list sederhana untuk isi di dalam list itu menjadi isi data untuk variable yang berbeda-beda
# Disebut:
# Unpack a Collection
fruit = ["Rambutan", "Jeruk", "Semangka"]
x,y,z = fruit
"""
Ini berguna untuk bila memiliki sebuah list dan sudah berisi data datanya dan ingin memasukannya kedalam sebuah variable maka menggunakan ini
"""

# VARIABLE GLOBAL
"""
Biasanya, ketika Anda membuat variabel di dalam suatu fungsi, variabel itu bersifat lokal, dan hanya dapat digunakan di dalam fungsi itu.

Untuk membuat variabel global di dalam suatu fungsi, Anda dapat menggunakan kata kunci global.
"""
# Contoh
x = "Awesome"
def myfunc():
    global x
    x = "Fantastic"
    print("Pyhton is " + x) #Ini adalah program yang global x nya berfungsi karena ada myfunc() didalamnya untuk mengaktifkan si fungsinya
myfunc()
print("Python is " + x)
####################################
x = "Cool"
def myFunc():
    global x
    x = "Bad"
    print("Python is " + x) # Ini adalah program yang global x nya tidak berfungsi karena tidak ada nya myFunc() / variable di fungsinya
                            # Sehingga fungsi globalnya tidak aktif    
 
print("Python is " + x)
"""
Kenapa di atas terdapat variable x itu Awesome dan Fantastic tetapi hanya menghasilkan Fantastic karena pada variable tersebut pada bagian
fungsi terdapat kata kunci global dan setelah itu x dirubah menjadi Fantastic , kan global pada fungsi itu berlaku kepada program disitu
sehingga si x terubah menjadi Fantastic tidak Awesome meskipun print nya di tetap yang berbeda, nah terkecuali si global tidak berlaku bila
variable pada si fungsi (def) tidak di panggil pada barisan yang sama dengan def myfunc()
"""

# PYTHON DATA TYPE
# TEXT TYPE = str
# Numeric Type = int, float, complex
# Sequence TYPE (Urutan) = list, tuple, range
# Mapping Type (Pemetaan) = dict
# Set Types = set. frozenset
# Boolean Type = bool
# Binary Types = bytes, bytearray, memoryview

# Contoh penulisannya
"""
str > x = "Hello World"
int > x = 20
float > x = 20.5 pake titik not koma karena kalo koma nanti masuknya jadi tuple
complex > x = 1j angka dan huruf sehingga lengkap atau complex
list > x = ["a","b","c"] menggunakan tanda kurung siku[]
tuple > x = ("a","B","c") menggunakan kurung biasa ()
range > x = range(6) menggunakan untuk tanda kurung biasa () dan berguna untuk mengatur jarak
dict > x = {"Name" : "b","c" : 36 } menggunakan tanda kurung kurawal {} dan : berguna untuk memanggil
set > x = {"A","B","C"} menggunakan tanda kurung kurawal{}
frozenset > x = frozenset ({"A","B"."C"}) berguna untuk membuka sebuat set
bool > x = True/False
bytes > x = b"Hello"
bytearray > x = bytearray(5)
memoryview > x = memoryview(bytes(5)) digunakan untuk melihat bytes
"""
# Contoh penulisan didalam pemogramannya
"""
str > x = str("Hello World")
int > x = int(20)
float > x = float(20.5) 
complex > x = complex(1j) 
list > x = list(("A","B","C"))
tuple > x = tuple(("a","B","c")) 
range > x = range(6) 
dict > x = dict(name="John", age=36) 
set > x = set(("A","B","C"))
frozenset > x = frozenset(("A","B","C)) 
bool > x = bool(5)
bytes > x = bytes(5)
bytearray > x = bytearray(5)
memoryview > x = memoryview(bytes(5))
"""

# Python Numbers
# INTERGER
# int
# Harus angka, boleh negatif atau positif, tidak boleh desimal, angka unlimited
# CONTOH
x = 1231231242
y = 1232124500523
z = -123231231
print(type(z))

# FLOAT
# float
# Harus angka, positif atau negatif, yang mengandung satu atau lebih desimal.
# CONTOH
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
# Float juga bisa berupa angka ilmiah dengan "e" untuk menunjukkan kekuatan 10. HANYA "E atau e" ya tidak boleh yang lain.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# COMPLEX
# Bilangan kompleks ditulis dengan "j" sebagai bagian imajiner
# CONTOH :
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Ternyata type data juga bisa di covert atau diganti formatnya
# Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Nah keren disini kita bisa mencari random number LOHH!!!!
# RANDOM NUMBER
# UNTUK RANDOM NUMBER INI SENDIRI DIA TIDAK MEMAKAI random() tetapi menggunakan module yaitu module random yang sudah tersedia di 
# library python itu sendiri
# CONTOH:
import random
print(random.randrange(1,100))
# nanti hasilnya akan random atau acak













