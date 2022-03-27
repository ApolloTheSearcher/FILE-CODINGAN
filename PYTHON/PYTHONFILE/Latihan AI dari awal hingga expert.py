# tentukan batas bilangan prima yang akan dicari
Angka = 50

#perulangan untuk mengecek bilangan prima
for num in range(2,Angka):
    prima = True
    for i in range(2,num):
        if (num%i==0):
            prima = False
    if prima:
       print (num)





