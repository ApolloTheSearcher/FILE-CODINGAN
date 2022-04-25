tinggi = 5
for t in range(tinggi) :
    for l in range(tinggi) :
        if((l == 0 and t == 0) or (l == 0 and t == tinggi - 1) or (l == tinggi - 1 and t == tinggi - 1) or
            (l == tinggi - 1 and t == 0)):
            print("o", end = "")
        elif (t == 0 or t == tinggi - 1) :
            print("-", end = "")
        elif (l == 0 or l == tinggi - 1) :
            print("|", end = "")
        elif (t == l) :
            print("\\", end = "")
        elif (l == tinggi - 1 - t) :
            print("/", end = "")
        else :
            print(" ", end = "")

    print()
