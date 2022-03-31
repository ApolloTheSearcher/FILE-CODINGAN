# pada bab ini Files disini bisa dilakukan oleh python
# Contohnya yaitu bila kita mempunya sebuah text (.txt) kita dapat membacanya menggunakan pyhton dengan menggunakan
"""
Caranya yaitu:
with open("Nama file txtnya") as nama_file_bebas:
    variable = nama_file_bebas.read()
print(variable)
"""
with open('tes.txt') as text_bebas:
    text_data = text_bebas.read()
print(text_data)

#selain itu kita juga dapat melakukan iterasi dengan menggunakan for looping
"""
with open('nama file txt') as nama_file_bebas:
    for nama_variable in nama_file_bebas.readlines()
print(variable)
"""
with open('tes.txt') as text_bebas1:
    for lines in text_bebas1.readlines():
        print(lines)
# Kita juga dapat mengambil first line atau second line atau line line yang lain dengan menggunakan .readlines()
"""
Menggunakan 
with open('namafile.txt') as nama_variable_bebas:
    first_line = nama_variable_bebas.readline()
    print(first_line)
"""

# Kita juga dapat langsung menulis kalimat baru ke file txt dengan menggunakan python
"""
with open('namafile.txt', 'w') as nama_variable_bebas: => w ini digunakan untuk write atau menulis
    nama_variable_bebas.write("Kalimat yang ingin di tulis")
"""


