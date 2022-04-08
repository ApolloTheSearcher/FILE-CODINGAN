# Deque
'''
Digunakan untuk menyimpan data secara terurut. jika semisalnya kita disuruh oleh seorang client untuk mengirimkan
data bug yang sangat besar nah client meminta kita untuk mengurutkannya dari kiri ke kanan ke kiri, berdasarkan
Jenis bug nya jika bugnya yang sangat besar (penting) maka otomatis di taruh di bagian kiri, jika bugnya yang ringan
maka akan di taruh setelah bug yang sangat penting tersebut. atau analoginya seperti berikut.
- Mari kita bayangkan situasi di mana kita sedang memproses dokumen besar yang berisi laporan bug untuk suatu
aplikasi. Untuk memprioritaskan bug yang paling penting, kami ingin semua laporan bug normal ditambahkan ke
akhir daftar dan bug dengan prioritas lebih tinggi berada di bagian depan daftar (seperti daftar prioritas).
Saat kami memperbaiki bug, mereka dapat dihapus dari bagian depan daftar.
Nah kita bisa mengimplementasikan dengan menggunakan deque.
- Contoh Programnya sebagai berikut:
'''
'''
bug_data = []

loaded_bug_reports = get_all_bug_reports()

for bug in loaded_bug_reports:
    if bug['priority'] == 'high':
        # A list uses the insert method to append to the front
        bug_data.insert(0, bug) # dimana pada proses ini jika bug yang penting akan di taruh di depan daftar
    else:
        bug_data.append(bug)

# A list must provide an index to pop
next_bug_to_fix = bug_data.pop(0) # yang dibaca yaitu dari bug yang paling kiri
'''
# Contoh jika kita menggunakan module deque
'''
from collections import deque

bug_data = deque()
loaded_bug_reports = get_all_bug_reports()

for bug in loaded_bug_reports:
    if bug['priority'] == 'high':
        # With a deque, we can append to the front directly
        bug_data.appendleft(bug) # Prosesnya hampir sama dengan insert hanya saja jika kita menggunakan ini maka lebih singkat penulisannya
    else:
        bug_data.append(bug)

# With a deque, we can pop from the front directly
next_bug_to_fix = bug_data.popleft() # yang dibaca yaitu dari bug yang paling kiri hanya saja penulisannya lebih mudah
'''
'''
Contoh Program lainnya:
from helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

# Write your code below!
# Checkpoint 1
supplies_deque = deque()
for data in csv_data:
    if data[2] == 'important':
        supplies_deque.appendleft(tuple(data))
    else:
        supplies_deque.append(tuple(data))

# Checkpoint 2
ordered_important_supplies = deque()
for order in range(25):
    ordered_important_supplies.append(supplies_deque.popleft())

# Checkpoint 3
ordered_unimportant_supplies = deque()
for ordered in range(10):
    ordered_unimportant_supplies.append(supplies_deque.pop())

# Cek
print(supplies_deque)
print(ordered_important_supplies)
print(ordered_unimportant_supplies)
'''

# Named Tuple
# Digunakan untuk menamai data yang ditampung dalam sebuah tuple. atau memberi parameter pada tuple.
# Koleksi Namedtuple memungkinkan kita untuk memiliki objek tuple yang tidak dapat diubah, 
# tetapi setiap elemen menjadi didokumentasikan sendiri.
# Contoh Programmnya
from collections import namedtuple
clothes = [('t-shirt', 'green', 'large', 9.99),
        ('jeans', 'blue', 'medium', 14.99),
        ('jacket', 'black', 'x-large', 19.99),
        ('t-shirt', 'grey', 'small', 8.99),
        ('shoes', 'white', '12', 24.99),
        ('t-shirt', 'grey', 'small', 8.99)]

# Write your code below!
ClothingItem = namedtuple('ClothingItem',['type', 'color', 'size', 'price']) #named tuplenya digunakan untuk membuat parameter 
                                                                            #nya sendiri

new_coat = ClothingItem('coat', 'black', 'small', 14.99) # sehingga nanti disini parameter harus sesuai urutan dengan namedtuple

coat_cost = new_coat.price
# Kita buat looping karena terlalu banyak biar mempermudah
updated_clothes_data = []
for data in clothes:
    updated_clothes_data.append(ClothingItem(data[0], data[1], data[2], data[3]))

print(updated_clothes_data)
