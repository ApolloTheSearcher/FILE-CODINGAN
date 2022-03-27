tinggi = 5
for m in range (tinggi):
    for n in range (tinggi):
        karakter = " "
        # if (n == 0 and m == 0) or (n == (tinggi - 1) and m == 0) or (n == (tinggi - 1) and m == (tinggi - 1)) or (n == 0 and m == (tinggi - 1)):
        #     karakter = "X"
        if (n == 0 or m == 0 or m == (tinggi - 1) or n == (tinggi - 1)):
            karakter = "O"
            
        print(karakter, end=" ")
    print()


n = 10
for t in range (n + 1):
    for l in range (n * 2):
        karakter = " "
        if l >= t and l < (n * 2)- t - 1:
            karakter = l - t
        print(karakter, end = " ")     
    print()