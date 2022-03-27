# print("Hello")
# print untuk menghasilkan string teks di console
# skrip itu nama file.py nya
# syntax itu code nya di dalam skrip
# Print("Hello")
# Print dengan P besar itu error karena belum ada fungsi dari si pythonnya dan kita bisa buat fungsi sendiri
# Case sensitive
# pada () difungsi print itu berguna untuk tempat input data.
# Literal itu data yang langsung ditulis oleh si programer
# Variable itu daya yang disimpan pada sebuah wadah.
# \n itu new line
# \r itu repeating

# hari = "Jumat"

# print(f"Hari ini adalah hari {hari}")
# Menggunakan f dan {} untuk memanggil variable tapi ketika run biasa bisa error tapi kita menggunakan Run and Debug
# variable menggunakan bahasa benda (noun)
# fungsi itu menggunakan bahasa kerja (verb)
# terus itu mengisi variable itu kita menggunakan (=) yang artinya itu assigment

# nama = "Alfian"
# umur = 22
# print("Nama saya,"+" " + nama +"." +"\nUmur saya"+ " " + str(umur), "tahun" + ".")
# cara supaya int itu ditambah dengan kontket bukan menjadi tambah operasi

# PR (PEKERJAAN RUMAH)

# Indomaret, Jl. Raya Perintis Kemerdekaan
# Nama Barang   Qty     Harga
#                              
#
#
#
#               Total = ................
#               Bayar = .................
#               Kembali = ...............

# INI BUAT FUNGSI PENGHITUNGANNYA.
barang = []
def ranjang(nama, quanty, harga):
    barang.append(
        {
            "namabarang" : nama,
            "quanty" : quanty,
            "harga" : harga
        }
    )
def kepalanya():
    print("Indomaret, Jl. Raya Perintis Kemerdekaan")
    print("Nama Barang", "Quantitiy", "Harga", sep="     \t")
def tabs(i):
    out = " "
    for _ in range (i):
        out += "\t"
    return out
def bayar(uang):
    kepalanya()
    total = 0
    for i in barang:
        total += i ["harga"] * i ["quanty"]
        print(i["namabarang"], i["quanty"], i["harga"], sep=" \t\t")
    print(tabs(8) + "Total= Rp."+"\t\t"+str(total))
    print(tabs(8) + "Bayar= Rp."+"\t\t"+str(uang))
    print(tabs(8) + "Kembalian= Rp."+"\t\t"+str(uang -total))
    
# Ibaratkannya sebagai ranjang pembelajaannya.
ranjang("Teh Botol",2, 10000)
ranjang("Indomie",4, 8000)
ranjang("Susu Beruang",6,8000)

bayar(200000)

###################################
        
# kepalanya
# bayar ("Nama Barang", quantity, harga)
# bayar ("Nama Barang", quantity, harga)
# bayar ("Nama Barang", quantity, harga)
# bayar ("Nama Barang", quantity, harga)
# bayar ("Nama Barang", quantity, harga)

# 5 barang, 5 harga, dan 5 quantity
































































































