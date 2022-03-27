import os
class Menu:
    # Static Field
    menus = None
    namaKelas = "====== Menu Smandak Cafe (logo Smandak) ======"
    
    
    
        # Static Method 
    def welcome():
        print("Selamat datang di Smandak Cafe\n\tSelamat Memesan\nPelanggan senang kamipun nyaman ")
    def inVoice():
        print("\t===== Demikian struk pembelian anda=====")
    def goodbye():
        print("Terimakasih telah mengunjungi Smandak Cafe\n\t== Jangan Bosan-Bosan Ya :) == ")
    def separator():
        print("===========================================================================================")
    def head():
        print("No" + "\tNama" + "\t\t\t" + "Harga" + "\t\t" "Stock")
    def namaMenu():
        print("\t\t MENU DARI SMANDAK CAFE")
    def goodbye():
        print("Terimakasih telah mengunjungi Smandak Cafe\n\t== Jangan bosan-bosan ya :) ==")
    
    # formatUang
    def formatUang(nilaiUang:int):
        after = ""
        before = str(nilaiUang)
        for i in range(len(before)):
            after += before[i]
            if((i + 1) % 3 == (len(before) % 3) and (i + 1) != len(before)):
                after += "."
        return "Rp." + after + ",-"

    # Tampilkan Menu
    def tampilanMenu():
        for i in range(len(Menu.menus)):
            print(f"{i + 1}. {Menu.menus[i].printItem()}")
    
    # BonBeli (static map)
    bonBeli = {

    }
    # Tampilkan BonBeli
    def cetakBonBeli():
        print("No." + "\t Nama" + "\t\t\t" + "Harga" + "\t\t\t" + "Stock")
        index = 1
        jumlahtTotalBeli = 0
        for key in Menu.bonBeli:
            print(f"{index} \t{key.printItemBon()} \t\t {Menu.bonBeli[key]}")
            index += 1
            jumlahtTotalBeli += Menu.bonBeli[key]
        Menu.separator()
        print(f"Total belanja jenis makanan kamu : {index - 1}")
        print(f"Total banyak belanja makanan kamu : {jumlahtTotalBeli}")
        print
        
            
            
            # Field
    def __init__(self, nama:str, harga:int, stock:int):
        # Constructor
        self.namaBarang = nama
        self.hargaBarang = harga 
        self.stockBarang = stock



            # Method
    def beli(self, jumlah:int):
        if(self.stockBarang >= jumlah):
            self.stockBarang -= jumlah
            if not self in Menu.bonBeli:
                Menu.bonBeli[self] = jumlah
            else:
                Menu.bonBeli[self] = Menu.bonBeli[self] + jumlah
                
            return True
        else:
            return False
    """
    def totalBelanja(self, totaljumlahbelanja:int):
        
    """    
        
    def printItem(self):
        tab = "\t"
        tab2 = "\t"
        if (len(self.namaBarang) <= 14):
            tab += "\t\t"
        else:
            tab += "\t"
        return(self.namaBarang + tab + Menu.formatUang(f"{self.hargaBarang}") + tab2 + f"{self.stockBarang}")
    def printItemBon(self):
        tab = "\t"
        if(len(self.namaBarang) <= 9):
            tab += "\t\t"
        else:
            tab += "\t"
        return (self.namaBarang + tab + Menu.formatUang(f"{self.hargaBarang}"))



# Daftar Menu
Menu.menus = [
    Menu("Nasi Goreng", 15000, 15),
    Menu("Seblak", 12000, 20),
    Menu("Cilok isi 12", 12000, 25),
    Menu("Es Teh", 3000, 30),
    Menu("Boba Coklat", 10000, 40),
    Menu("Boba Strawberry", 10000, 50)
]