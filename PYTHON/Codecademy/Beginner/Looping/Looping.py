# Cara penulisan jenis looping di python
'''
ini dibawah digunakan untuk for looping in tidak dengan range
for <temporary variable> in <collection>:
    <action>
    
ini dibawah digunakan untuk for looping in dengan range
for <temporary variable> in range<awal,akhir,step>:
    <action>
    
ini dibawah digunakan untuk looping dengan while
while <condition statement>:
    <action>
    
# List comprehension (looping)
new_list = [<expression> for <element> in <collection>]
jika ingin langsung lebih mudah menulis loopingnya
tapi harus ada yang diketahui yaitu:
1. Mengambil elemen dalam nomor daftar
2. Menetapkan elemen itu ke variabel yang disebut num (<elemen> kami)
3. Menerapkan <expression> pada elemen yang disimpan dalam num dan menambahkan hasilnya ke daftar baru yang disebut doubled
4. Ulangi langkah 1-3 untuk setiap elemen lain dalam daftar angka (<koleksi> kami)

# List comprehension conditional (looping)
sama dengan yang di atas hanya saja dia terdapat control flow atau kondisi tertentu
new_list = [<expression> for <element> in <collection> if <condition> else <default value>]
'''