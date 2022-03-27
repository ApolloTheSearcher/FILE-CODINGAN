'''
Global namespace dibawah built-in namespace
ni mencakup semua nama non-bersarang dalam modul (file) yang kami pilih untuk menjalankan interpreter Python.
Namespace global dibuat ketika kami menjalankan program utama kami dan memiliki masa pakai hingga interpreter
berakhir (biasanya ketika program kami selesai dijalankan).
Seperti kaya kita bisa ngisi sendiri gitu kalau global namespace.
Skrip kami terdiri dari beberapa variabel berbeda, fungsi, dan modul yang diimpor. Langsung saja, mungkin tidak
jelas apa yang ada di namespace global. Untungnya, untuk melihat objek apa yang ada di namespace global, Python menyediakan fungsi bawaan globals().
Cukup lucu, fungsi globals() sebenarnya berasal dari namespace bawaan (dan dengan demikian disebut fungsi bawaan),
dan kita dapat mengaksesnya di mana saja di program kita (atau program apa pun)!
Jadi ketika kita menambahkan variable atau import atau yang lain itu bisa masuk kedalam global namespace.
Contoh perogram yang menggunakan global namespace :
'''
print(' -- Globals Namespace with empty script -- \n')
# Checkpoint 1
print(globals()) # fungsi untuk melihat global namespace

# Checkpoint 2
global_variable = 'global'

# Checkpoint 3
def print_global():
    global_variable = 'nested global'
    nested_variable = 'nested value'

# Checkpoint 4
print(' \n -- Globals Namespace non-empty script -- \n')
print(globals())








