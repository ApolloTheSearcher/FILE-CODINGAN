'''
Pada itertools finite juga terdapat lumayan banyak salah satunya itu yang akan kita pelajari disini chain()
Sebuah Finite Iterator akan berakhir berdasarkan panjang dari satu atau lebih nilai input.
Finite Iterator sangat bagus untuk bekerja dengan dan memodifikasi iterator yang ada.
Itertool yang berguna yang merupakan Finite Iterator adalah chain() itertool. Iterator terbatas ini akan
mengambil satu atau lebih iterable dan menggabungkannya menjadi satu iterator.
- Penulisannya:
chain(*iterables) => penulisan chain() untuk iterables adalah variable yang isinya berupa apa aja

Contoh programnya:
'''
import itertools

great_dane_foods = [2439176, 3174521, 3560031]
min_pin_pup_foods = [6821904, 3302083]
pawsome_pup_foods = [9664865]

# Write your code below: 
all_skus_iterator = itertools.chain(great_dane_foods, min_pin_pup_foods, pawsome_pup_foods)

for i in all_skus_iterator: # Menggunakan for in all_skus_iterator untuk mengambil nilai satu per satu
    print(i)