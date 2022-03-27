'''
Rekap kembali:
pada sebuah fungsi itu ada 3 macam penulisan fungsi argument
yaitu 
1. Positional Argument: argumen yang dipanggil oleh posisinya dalam definisi fungsi
2. Keyword Argument: argumen yang disebut dengan namanya
3. Default Argument: argumen yang tidak diberikan, tetapi di definisi fungsi kita dapat menggunakan nilai default
Contoh:
'''
# 1 Positional Argument:
def print_name1(first_name, last_name):
    print(first_name, last_name)
# Kita panggil
print_name1("Gentha", "Ardaana")
'''
Di sini, first_name akan dipetakan ke 'Gentha' sedangkan last_name akan dipetakan ke 'Ardaana' karena posisi
argumen saat memanggil fungsi.
'''

# 2 Keyword Argument:
def print_name2(first_name, last_name):
    print(first_name, last_name)
# Kita panggil
print_name2(first_name="Gentha", last_name="Ardaana")
'''
Di sini, kita menggunakan nama parameter first_name dan last_name sebagai argumen kata kunci dalam pemanggilan
fungsi. Perhatikan urutan argumen tidak masalah karena mereka diberi nama tertentu.
'''

# 3 Default Argument:
def print_name3(first_name = "Gentha", last_name = "Ardaana"):
    print(first_name, last_name)
# Kita panggil
print_name3()
'''
Di sini, dalam definisi fungsi, kami menetapkan nilai default ke parameter. Ini berarti kita dapat memanggil
fungsi kita tanpa memberikan argumen apa pun karena mereka akan memiliki nilai untuk digunakan kembali.
'''
# Contoh Case:
tables = {
    1: ['Jiho', False],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
}
print(tables)

# Write your code below: 
def assign_table(table_number, name, vip_status = False):
    tables[table_number] = [name, vip_status]

# Table point 6 = Positional Argument
assign_table(6, "Yoni", False)

# Table point 3 = Keyword Argument
assign_table(table_number = 3, name = "Martha", vip_status = True)

# Table point 4 = Default Argument
assign_table(4, "Karla")
print(tables)