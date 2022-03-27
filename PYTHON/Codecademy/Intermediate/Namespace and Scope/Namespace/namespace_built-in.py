'''
Didalam program python itu terdapat 4 tipe ruang utama yaitu :  built-in namespace, Global namespace, local/enclosing namespace
nah salah satunya built-in namespace. seperti fungsi print, len, type, dll tersedia untuk semua program kita itu mereka mengambil dari
ruang utama ini loh. nama-nama fungsi ini karena mereka ada di tingkat tertinggi ruang nama dan dengan demikian
dapat dipanggil dalam program apa pun yang kita tulis.
Setiap kali kami menjalankan aplikasi Python, kami disediakan namespace built-in yang dibuat saat interpreter
dimulai dan memiliki masa pakai hingga interpreter berakhir (biasanya saat program kami selesai dijalankan).
Karena Python menyediakan namespace, objek ini dapat diakses tanpa perlu mengimpor modul terpisah.
Kita bisa liat salah satu build-in namespace yang ada di Python :
'''
print(dir(__builtins__)) # dir() untuk menampilkan nama-nama fungsi yang ada di built-in namespace python yang biasa kita pakai
'''
Total ada 152 nama yang mencakup pengecualian, fungsi, tipe, atribut khusus, dan objek bawaan Python lainnya.
1. Ini berisi banyak fungsi bawaan yang dapat kita gunakan dalam program Python seperti str(), zip(), slice(),
sort(), dan banyak lagi.
2. Itu juga menampung banyak pengecualian yang mungkin kita temui dalam program kita seperti 'ArithmeticError',
'IndexError', 'KeyError', dan banyak lagi.
3. Bahkan ada konstanta seperti Benar dan Salah!
'''

