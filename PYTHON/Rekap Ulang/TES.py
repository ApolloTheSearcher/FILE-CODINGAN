angka1 = int(input("Masukan angka 1: "))
angka2 = int(input("Masukan angka 2: "))

# IF STATEMENT
if angka1 == angka2:
    print(f"{angka1} sama dengan {angka2}")
if angka1 > angka2:
    print(f"{angka1} lebih dari {angka2}")
if angka1 < angka2:
    print(f"{angka1} kurang dari {angka2}")
if angka1 >= angka2:
    print(f"{angka1} lebih dari sama dengan {angka2}")
if angka1 <= angka2:
    print (f"{angka1} kurang dari sama dengan {angka2}")
    
# Dibawah menggunakan Method Formatting
if angka1 != angka2:
    print("{} tidak sama dengan {}".format(angka1, angka2))
