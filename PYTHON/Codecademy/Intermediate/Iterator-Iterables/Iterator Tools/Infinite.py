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
    if counts >= max_capacity:
        break
    num_bags += 1
print(num_bags)