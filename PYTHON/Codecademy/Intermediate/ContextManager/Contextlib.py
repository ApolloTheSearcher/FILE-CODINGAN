# Sebelumnya ClassBasedContext Manager kita dapat membuat Manager Context dengan menggunakan class.
# Dengan menggunakan __enter__ dan __exit__ tetapi selain itu kita dapat menggunakan method __init__
# Tetapi terdapat cara mudahnya loh tanpa class based loh. yaitu dengan menggunakan metode Contextlib
'''
Modul ini contextlib memungkinkan pembuatan manajer konteks dengan penggunaan fungsi generator
(fungsi yang menggunakan yieldalih-alih return) dan dekorator contexlib - @contextmanager.
Alih-alih membuat kelas dan mendefinisikan __enter__dan __exit__metode, kita dapat menggunakan fungsi
sederhana!
Menggunakan import contextmanager dari contextlib

Setelah kita berhasil mengimpor modul, kita dapat secara otomatis menggunakan @contextmanagerdekorator untuk
membungkus fungsi generator.
Contoh program:
'''
# Write your code below:
from contextlib import contextmanager

@contextmanager # Jadi disini kita tidak perlu membuat class untuk menggunakan context manager
# Karena sudah menggunakan @contextmanager
def poem_files(file, mode):
    print("Opening File")
    open_poem_file = open(file, mode)
    try:
        yield open_poem_file
    finally:
        print('Closing File')
        open_poem_file.close()
    
with poem_files('poem.txt', 'a') as opened_file:
    print('Inside yield')
    opened_file.write('Rose is beautiful, Just like you.')

'''
Setelah kita membuat fungsi ini dan menyatakannya sebagai pengelola konteks menggunakan @contextmanager 
dekorator, kita dapat langsung menggunakannya seperti sebelumnya dalam sebuah with
'''

# Exception Handling Contextlib
from contextlib import contextmanager

@contextmanager
def poem_files(file, mode):
    print('Opening File')
    open_poem_file = open(file, mode)
    try:
        yield open_poem_file
#Write your code below: 
    except AttributeError as e: # pada contextlib juga kita dapat menambahkan exception handling
        print(e) # Dimana gunanya untuk menangani error yang terjadi dan memberitahu kita bahwa error tersebut

    finally:
        print('Closing File')
        open_poem_file.close()

with poem_files('poem.txt', 'a') as opened_file:
    print('Inside yield')
    opened_file.sign('Buzz is big city. big city is buzz.')

# Nested Context Manager
'''
Pada contoh contoh sebelumnya bahwa kita hanya menggunakan context manager dalam context dari satu file
sedangkan bagaimana jika with itu menyimpan lebih daru satu file.
Untuk mencapai tujuan tersebut dengan banyak sumber daya sekaligus, manajer konteks dapat disarangkan bersama
dalam sebuah withpernyataan untuk mengelola banyak sumber daya secara bersamaan.
Contoh programnya:
'''
from contextlib import contextmanager
@contextmanager
def poem_files(file, mode):
    print('Opening File')
    open_poem_file = open(file, mode)
    try:
        yield open_poem_file
    finally:
        print('Closing File')
        open_poem_file.close()


@contextmanager
def card_files(file, mode):
    print('Opening File')
    open_card_file = open(file, mode)
    try:
        yield open_card_file
    finally:
        print('Closing File')
        open_card_file.close()

# Write your code below:
with poem_files('poem.txt', 'r') as poem: # Disini terdapat nested context manager dimana kita mengakses 2 file
    with card_files('card.txt', 'w') as card: # dan didalam with itu terdapat 2 argumen dimana isinya itu
        print(poem, card) # yang pertama itu adalah nama filenya dan argument yang 2 itu adalah mode nya
        card.write(poem.read()) # r itu artinya read dan w itu artinya write.

