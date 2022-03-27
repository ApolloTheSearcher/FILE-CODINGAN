# Reduce()
'''
Fungsi tingkat tinggi reduce() adalah fungsi yang memiliki parameter fungsi dan iterable.
Berbeda dari tingkat tinggi bawaan lainnya bahwa reduce() itu bisa digunakan ketika kita mengimport module
dari functools baru bisa menggunakan fungsi reduce()
Daripada mengembalikan objek reduksi seperti yang diharapkan setelah mempelajari tentang map() dan filter(),
reduce() mengembalikan satu nilai. Untuk mendapatkan nilai tunggal ini, reduce() secara kumulatif
menerapkan fungsi yang diteruskan ke setiap pasangan elemen berurutan dalam iterable.
cara penulisan reduce() => nama_variable = reduce(function, iterable)

Contoh case dimana kita ingin menggabungkan sebuah string didalam array menjadi sebuah kalimat string menggunakan
fungsi reduce()
'''
# Dibawah adalah contoh penggunaan reduce() tanpa lambda
from functools import reduce
letters = ['r', 'e', 'd', 'u', 'c', 'e']

# your code below:

# remember to import the reduce function
def words(x, y):
    return x + y

# store the result of your reduce function in the variable word
word = reduce(words, letters)


# print word
print(word)

# Output: reduce

# Dibawah adalah contoh penggunaan reduce() dengan lambda
# your code dengan lambda:

# store the result of your reduce function in the variable word
word = reduce(lambda x,y : x + y, letters)
# x,y adalah parameter fungsinya ya guys

# print word
print(word)

# Output: reduce