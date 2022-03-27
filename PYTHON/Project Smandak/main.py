
from menu import Menu
import os
if __name__ == "__main__":
    uang = 3000000
    os.system("clear")
    print(Menu.namaKelas)
    Menu.welcome()
    Menu.separator()
    Menu.namaMenu()
    Menu.head()
    Menu.tampilanMenu()
    
    while(True):
        Menu.separator()
        print(f"Pilihan pesanan [1 - {len(Menu.menus)}] [ q - keluar(selesai membeli)] [m - lihat menu] ")
        cek = str(input("Pilih : "))
        if(cek == "q"):
            break
        elif(cek == "m"):
            os.system ("clear")
            print(f"Sisa Uang Kamu: {Menu.formatUang(uang)}")
            Menu.separator()
            Menu.namaMenu()
            Menu.head()
            Menu.tampilanMenu()
            continue
        
        pilihan = int(cek)
        if((pilihan > 0) and (pilihan <= len(Menu.menus))):
            terpilihan = Menu.menus[pilihan - 1]
            print(">> " + terpilihan.printItem())
            Menu.separator()
            jumlah = int(input("Jumlah pesanan :"))
            print(f">> {jumlah} porsi")
            subtotal = terpilihan.hargaBarang * jumlah
            if(subtotal <= uang):
                if(terpilihan.beli(jumlah)):
                    print(f"Kamu membeli {terpilihan.namaBarang} seharga {Menu.formatUang(subtotal)}"
                    )
                    uang -= subtotal
                else:
                    print("Maaf stock habis :)")
                if(uang > 0):
                    print("Sisa uang : " + Menu.formatUang(uang))
                else:
                    print("Uangmu Habis!!!")
            else:
                print("Maaf uangmu tidak cukup")
    os.system("clear")
    Menu.inVoice()
    Menu.separator
    Menu.cetakBonBeli()
    Menu.separator()
    Menu.goodbye()
