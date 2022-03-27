#BLOK PROGRAM SEGITIGA KEBALIK

# tinggi = int(input("Masukan ukuran untuk segitiganya: "))
tinggi = 4
for t in range (tinggi):
    for l in range (tinggi * 2 - 1):
        karakter = " "
        if l >= t and l < (tinggi * 2)- t - 1:
            karakter = l
        print(karakter, end = " ")     
    print()