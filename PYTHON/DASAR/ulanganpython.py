# MATERIIIIIII

# data1 = "Halo, selamat siang"
# hasilSplit1 = data1.split(" ")
# print(hasilSplit1)
# tanda kutip di atas berguna untuk memisahkan kata pada kalimat
# di data1 hanya saja nantinya koma disetiap kata berada di dalam
# tanda kutipnya

# data2 = "Bayam, Tomat, Lengkuas, Jahe"
# hasilSplit2 = data2.split(", ")
# Koma didalam tanda kutip tersebut berguna untuk supaya nanti 
# mensplit kata maka komanya terdapat di luar tanda kutip setiap
# kata-kata
# print(hasilSplit2)

# KALIAN DAPAT MENGGUNAKAN .SPLIT PADA STRING UNTUK MEMISAHKAN
# SEBUAH KALIMAT.

# UNTUK MENGGABUNGKAN SELURUH KALIMAT YANG BERADA PADA SPLIT
# DAPAT MENGGUNAKAN "isi apa yang akan di tambahkan didalam split ".join(ini variable yang di .split)

# MISALKAN PADA DATA 2
# data2 = " : ".join(hasilSplit2)
# print(data2)
# # MISALKAN PADA DATA 1
# data1 = "+".join(hasilSplit1)
# print(data1)

# REVERSE KALIMAT ULANGAN PYTHON

# import math
# import os
# import random
# import re
# import sys

# if __name__ == '__main__':
#     tipe = input()
#     data = str(input())
    
    
#     if (tipe == "True"):
#         print("".join(reversed(data)))
        
#     else:
#         list_data = []
#         kata = ''
#         for i in data:
#             if i != ' ':
#                 kata += i
#             else:
#                 list_data.append(kata)
#                 kata = ''
#         list_data.append(kata)
#         list_ku = list_data[::-1]
#         data2 = " ".join(list_ku)
#         print(data2)
#     print()



# Deretan Bilangan Fibonacci


#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'generateFibonacci' function below.
#
# The function accepts INTEGER i as parameter.
#
# def generateFibonacci(i):
    # Write your code here
#     fib = [0,1]
#     for j in range (i - 2):
#         fib.append(fib[j] + fib[j+1])
#     print(fib)    

# if __name__ == '__main__':
#     i = int(input().strip())

    # Fungsi untuk mendapatkan deret bilangan fibonacci sebanyak i
    # generateFibonacci(i)
    
    
# Jumlah Deret Bilangan Prima
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'totalPrime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

# def totalPrime(n):
#     banyak = 0
#     angka = 2
#     prime = []
#     while(banyak < n):
#         prima=True
#         for i in range(2,angka):
#             if(angka%i==0):
#                 prima = False
#         if (prima):
#             banyak += 1
#             prime.append(angka)
#         angka+=1
#     hasil = sum(prime)
#     return hasil
        

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     val = totalPrime(n)

#     fptr.write(str(val) + '\n')

#     fptr.close()











