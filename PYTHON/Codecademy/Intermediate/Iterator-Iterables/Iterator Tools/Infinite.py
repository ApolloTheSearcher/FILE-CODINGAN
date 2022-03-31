# Disini kita akan membahas tools yang ada pada infinite yaitu salah satunya count()
"""
Iterator tak terbatas akan mengulangi jumlah tak terbatas tanpa titik akhir dan tanpa pengecualian
StopIteration yang dimunculkan. Iterator tak terbatas berguna saat kita memiliki aliran data tak terbatas
untuk diproses.
Itertool yang berguna yang merupakan iterator tak terbatas adalah count() itertool. Iterator tak terbatas ini
akan menghitung dari nilai pertama hingga kami menyediakan beberapa jenis kondisi berhenti.

Kita sebelumnya menggunakan fungsi count() kita wajib mengimport dulu ya!
import itertools
.count(start, [step]) => penulisan count()
"""
# Contoh program:
import itertools
max_capacity = 1000
num_bags = 0
for counts in itertools.count(start = 13.5, step = 13.5):
    # menggunakan ^^^^^^^^^^ di atas itu hanya bisa menggunakan itertools ya untuk memanggil fungsi dari module
    # itertools
    if counts >= max_capacity: # Jika nilai counts lebih besar dari max_capacity, maka akan berhenti
        break
    num_bags += 1 # Increment dari num_bags
print(num_bags)