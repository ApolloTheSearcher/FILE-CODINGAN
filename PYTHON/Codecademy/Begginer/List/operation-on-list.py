# Terbagi menjadi banyak operasi yang bisa dilakukan pada list
'''
1. Append (.append())
2. Remove (.remove())
3. Count (.count())
4. Insert (.insert())
5. Sort (.sort()) /Sorted (.sorted())
6. Pop (.pop())
7, Range (.range())
8. Reverse (.reverse())
9. Lenght (.len())
10. Index (.index())
'''
# Insert a value at the end of a list
# memungkinkan kita untuk menambahkan elemen ke indeks tertentu dalam daftar.
# Insert itu lebih luas dari append kan kalau append itu hanya cukup menambahkan list di akhir
# Cara penulisan insert itu biasanya menggunakan indeks yang ditentukan.
# Contoh:
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
# Kita ingin menambahkan nama namun ingin nanti namanya ada di index ke 2 maka kita gunakan insert
store_line.insert(2, "Nadia")
print(store_line)
# 2 disitu untuk menambahkan nama nadia di index ke 2
# Hal-hal yang perlu diperhatikan:
'''
1. Metode.insert() mengharapkan dua input, yang pertama adalah indeks numerik, diikuti oleh nilai apa pun sebagai input kedua.
2. Ketika kita memasukkan elemen ke dalam daftar, semua elemen dari indeks yang ditentukan dan hingga indeks terakhir digeser satu indeks ke
kanan. Ini tidak berlaku untuk memasukkan elemen ke akhir daftar karena hanya akan menambahkan indeks tambahan dan tidak ada elemen lain
yang perlu bergeser.
'''

# Removing by index : Pop
'''
Digunakan untuk menghapus elemen dari daftar.
dan menjadikan dia sebuah nilai baru yang keluar dari list
Cara menghapus elemennya itu dengan menambahkan didalam pop index list yang ingin di hapus
Namun jika kita tidak mengisi data index didalam pop yang ingin di hapus maka nanti yang akan terhapus itu adalah index terakhir
'''
# Contoh:
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
removed_element = cs_topics.pop() # => contoh jika kosong pada fungsi pop
print(cs_topics)
print(removed_element)
# Output
# ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
# 'Clowns 101'

# Consecutive List : Range
'''
Digunakan untuk membuat list dengan jarak yang ditentukan


'''

# Operation Zip (.zip())
'''
digunakan untuk membuat atau menggabungkan 2 list menjadi 1 data list yang sama panjang
'''
# Contoh:



# Jika kita ingin menambahkan isi list dengan operasi pertambahan jangan lupa + [data yang mau ditambahin ke list]



