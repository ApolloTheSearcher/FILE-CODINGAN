# penggunaan lt, gt, le, ge, eq, ne
# lt = less than ( < )
# gt = greater than ( > )
# le = less than or equal to ( <= )
# ge = greater than or equal to ( >= )
# eq = equal to ( == )
# ne = not equal to ( != )
# Implementasi dari operator ini dapat dilihat pada kasus jumlah kelereng berwarna hijau dan kuning.
from operator import *
hijau = 5
kuning = 10
print("Kelereng Hijau = {}".format(hijau))
print("Kelereng Kuning = {}".format(kuning))
for func in (lt, gt, le, ge, eq, ne):
    print("{}(hijau,kuning): {}".format(func.__name__, func(hijau, kuning)))
# Outputnya :
# Kelereng Hijau = 5
# Kelereng Kuning = 10
# lt(hijau, kuning): True
# le(hijau, kuning): True
# eq(hijau, kuning): False
# ne(hijau, kuning): True
# ge(hijau, kuning): False
# gt(hijau, kuning): False

# cara singkat menuliskan operasi
# Jika anda melakukan assignment kembali hasil sebuah expression, beberapa di antaranya bisa disingkat sebagai berikut:
a = 2
a = a + 4
# disingkat menjadi:
a = 2
a += 4

# Urutan matematis dalam melakukan evaluasi
# Tip = Gunakan kurung untuk memudahkan penggunaan keterbacaan dan memastikan urutan secara tepat.
# contoh:
print (2+(3*4))
# Operator di python juga bersifat asosiatif dari kiri ke kanan.
