# Cara membuka sebuah file menggunakan sumber daya di Python
# Contoh:
try:
    open_file = open('file_name.txt', 'r') # file_name.txt adalah nama file yang akan dibuka
    print(open_file.read())
finally: # Jika tidak menggunakan finally maka file akan dibuka terus menerus
    open_file.close()

with open('file_name.txt', 'r') as open_file: # Menggunakan context manager dan menetapkan nama file yang akan dibuka
    print(open_file.read())
    
# Class Based Context Manager
'''
Salah satu dari dua pendekatan untuk create context manager disebut Class Based Context Manager.
Class based ini menulis manager konteks memerlukan secara eksplisit mendefinisikan dan mengimplementasikan
dua method berikut:
- __enter__():
Metode __enter__ini memungkinkan penyiapan manajer konteks. Metode ini biasanya menangani sumber daya yang
terbuka (seperti file)
- __exit__():
__exit__Memastikan kerusakan manajer konteks . Metode ini biasanya menangani penutupan sumber daya terbuka 
yang tidak lagi digunakan. pada __exit terdapat dua parameter yaitu self, *exc dimana ini untuk mengatur bila ada kerusakan
Contoh Program:
'''
# Write your code below: 
class PoemFiles:
    def __init__(self):
        print('Creating Poems!')
    def __enter__(self):
        print('Opening poem file')
    def __exit__(self,*exc):
        print('Closing poem file')

with PoemFiles() as manager:
    print('Hope is the thing with feathers')
'''
Kemudian selain itu kan di atas terdapat method __init__ dimana itu yang akan menyimpan parameter untuk membuka
file. Metode ini standar di sebagian besar kelas, bahkan yang bukan manajer konteks itu sendiri.
Contoh lainnya:
'''

# Write your code below:
class PoemFiles:
    def __init__(self, poem_file, mode):
        print('Starting up a poem context manager')
        self.file = poem_file
        self.mode = mode # Pada init disini digunakan untuk mendeklarasikan sebuah parameter untuk digunakan 
        # di method lainnya
    def __enter__(self):
        print('Opening poem file')
        self.opened_poem_file = open(self.file, self.mode) # Disini kita membuat method supaya nanti bisa diakses
        return self.opened_poem_file
    def __exit__(self, *exc):
        print('Closing poem file')
        self.opened_poem_file.close()

with PoemFiles('poem.txt', 'w') as open_poem_file: # didalam parameter PoemFiles adalah method dari __enter__
    open_poem_file.write('Hope is the thing with feathers')


# Handling Exceptions
# Contoh program:
class PoemFiles:

    def __init__(self, poem_file, mode):
        print(' \n -- Starting up a poem context manager -- \n ')
        self.file = poem_file
        self.mode = mode

    def __enter__(self):
        print('Opening poem file')
        self.opened_poem_file = open(self.file, self.mode)
        return self.opened_poem_file

# Create your __exit__ method here:
    def __exit__(self, exc_type, exc_value, traceback): # Selain tanda * di parameter __exit__
        print(exc_type) # kita juga dapat mengisi dengan berapa keadaan ketika error
        print(exc_value)
        print(traceback)
        self.opened_poem_file.close()
'''
Ketiga jenis argumen ini yaitu:
- exc_type: yang menunjukan class pengecualian errornya seperti AtributeError class, atau NameError class
- exc_value: menunjukan nilai sebenarnya dari kesalahan yang terjadi/error
- traceback: laporan yang merinci urutan langkah yang menyebabkan kesalahan dan semua detail yang diperlukan
untuk memperbaiki kesalahan.
'''

# First
# with PoemFiles('poem.txt', 'r') as file:
#   print("---- Exception data below ----")
#   print(file.uppercasewords())
# .uppercasewords() not a real method
'''
Jika kita menjalakan program First akan terjadi error karena pada file.uppercasewords() itu memang dia akan exc_type
karena methodnya tidak ada. kemudian akan di traceback errornya dan diberikan detailnya untuk memperbaiki kesalahan.
'''

# Second
with PoemFiles('poem.txt', 'r') as file2:
    print(file2.read())
    print("---- Exception data below ----")

# Handling Exceptions contoh lain:
'''
Selain cara di atas cara mengatasi exception pada method __exit__ tetapi terdapat method lagi selian itu:
Jika kita ingin melempar kesalahan saat terjadi kesalahan, kita dapat:
return False setelah .close()metode
Tidak melakukan apapun

Jika kita ingin menekan kesalahan, kita dapat:
return True setelah .close() metode
'''


class PoemFiles:

    def __init__(self, poem_file, mode):
        print(' \n -- Starting up a poem context manager -- \n')
        self.file = poem_file
        self.mode = mode

    def __enter__(self):
        print(' \n --  Opening poem file -- \n')
        self.opened_poem_file = open(self.file, self.mode)
        return self.opened_poem_file

    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type, exc_value, traceback, '\n')
    # Write your code below:
        if isinstance(exc_value, AttributeError): # Disini untuk mengecek pada percobaan pertama
            self.opened_poem_file.close() # dimana artinya jika pada exc_value itu ada AttributeError
            return True # maka dia akan menekan kesalahannya

with PoemFiles('poem.txt', 'r') as file:
    print("---- Exception data below ---- \n ")
    print(file.uppercasewords())

with PoemFiles('poem.txt', 'r') as file2:
    print(file2.read())
    print(" \n ---- Exception data below ---- \n ")

