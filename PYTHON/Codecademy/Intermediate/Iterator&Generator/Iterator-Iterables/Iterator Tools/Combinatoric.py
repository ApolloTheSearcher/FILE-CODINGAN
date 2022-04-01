'''
Iterator kombinatorik akan melakukan serangkaian operasi statistik atau matematika pada input yang dapat diubah.
Iterator yang berguna yang merupakan iterator kombinatorial adalah kombinasi() iterator.
- Penulisannya:
combinations(iterable, r) => penulisan combinations() untuk nilai iterable adalah variable yang isinya berupa
apa aja dan nilai r itu adalah yang mewakili panjang setiap kombinasi tupel. 
Hasil return dari combinations() adalah iterator yang dapat digunakan dalam for loop atau dapat diubah menjadi
tipe iterable menggunakan list() atau set().
Contoh Case:
'''
import itertools

collars = ["Red-S","Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

# Write your code below: 
collar_combo_iterator = itertools.combinations(collars, 3)
# Nilai collars itu adalah variable yang isinya berupa apa aja
# Nilai 3 adalah r yang mewakili panjang setiap kombinasi tupel
for i in collar_combo_iterator:
    print(i)