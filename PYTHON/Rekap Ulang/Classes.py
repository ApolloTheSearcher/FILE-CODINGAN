class Pohon:
    jumlahPohon = 0
    jumlahtotalDaun = 0
# ini adalaah static data jadi gk usah pake static lagi kalo di python.
    def __init__(self, panjangBatang:int, jumlahBuah:int, jumlahDaun:int, namaPohon:str):
        # ini hanya membantu memberitahu saja
        # bukan untuk memastikan
        self.panjangBatang = panjangBatang
        self.jumlahBuah = jumlahBuah
        self.jumlahDaun = jumlahDaun
        self.namaPohon = namaPohon
        Pohon.JumlahDauntotal += jumlahDaun
        # untuk menambahkan jenis data pada class python itu tambahnya
        # di constructornya
    # digunakan untuk membuat constructor (initializer)
    # self itu ibaratkan this untuk memasukan input kedalam nilai constructornya
    #############################################################################
    # Cara membuat method pada class python
    def tumbuh(self):
        self.panjangBatang += 1
        self.jumlahBuah += 1
        self.jumlahDaun +=1
    # diatas adalah method biasa
    # dibawah ini adalah contoh membuat method static di python.
    def nama():
        return "Pohon"
    # pada method static didalam kurungnya itu tidak memakai self
    # kalau di python Static dan biasa tetap ketika memanggilnya menggunakan
    # kalau biasa memakai self
    # kalau Static memakai nama classnya

if __name__ == "__main__":
    print("Hello World")
    pohon1 = Pohon(10, 20, 30, "Pohon1")
    print(pohon1.jumlahBuah)
# kalau kita ingin mengambil data biasa bukan static kita printnya objeknya aja.
    print(Pohon.jumlahPohon)
# Kalau kita ingin mengambil data static kita print panggilnya itu nama classnya.
    pohon1.tumbuh()
    # diatas digunakan untuk mengaktifkan method tumbuh
    print(pohon1.panjangBatang)
    print(pohon1.jumlahDaun)
    
















# instance itu Objek yang dibuat dari class
# Literal itu data yang langsung di masukan atau ditulis oleh program
# atau diketik manual.