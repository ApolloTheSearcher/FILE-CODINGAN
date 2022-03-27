'''
Python juga memiliki hal spesial yaitu unpacking & beyond
digunakan untuk membukus suatu list kedalam argumen fungsi
contoh penggunaannya
'''
def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)

# Write your code below:
table_7_total = [534.50, 20.0, 5] # => [total, tip, split] didalam list ini berisi argument untuk fungsi

calculate_price_per_person(*table_7_total) # => unpacking si listnya membungkus

########################################################################################################################
'''
Selain itu kita juga bisa menggunakan unpacking ini untuk mengetahui range dari suatu list
Contoh programmnya:
'''
start_and_stop = [3, 6] # => [start, stop] didalam list ini berisi argument untuk fungsi

range_values = range(*start_and_stop) # fungsi range ini membungkus listnya 3 sebagai awal, dan 6 akhirnya
print(list(range_values)) # => mengambil range dari 3 sampai 6 outputnya adalah [3, 4, 5]

