print("PROGRAM MEMASUKAN ANGKA RANDOM AKAN MENGHASILKAN NAMA RANDOM")
angka = int(input("Masukkan angka : "))
kalimat = "Boy"

if(angka < 0):
    kalimat += "Bad"
    if(angka % 2 == 0):
        kalimat = kalimat + "Beni"
    elif(angka % 2 == 1):
        kalimat = kalimat + "Boy"
else:
    if(angka % 2 == 0):
        kalimat = kalimat + "Beni"
    elif(angka % 2 == 1):
        kalimat = "Budi" + kalimat
    else:
        kalimat = "Becca"
    kalimat = kalimat + "Billiard" + kalimat
    
if(len(kalimat)>5):
    kalimat = kalimat + "s"
    if(angka - 10 > 0):
        kalimat = "Becca" + kalimat
    else:
        kalimat = kalimat + "Becca"
elif(len(kalimat)<5):
    kalimat = "Belly" + kalimat
    
print(kalimat)