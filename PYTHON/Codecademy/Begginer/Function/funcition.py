'''
Penulisan fungsi di python itu menggunakan def
def nama_fungsi(parameter):
    # kode yang akan dijalankan => jika kita tidak menuliskan kode di dalam fungsinya maka bisa jadi error

kemudian cara pemanggilan function tanpa return yaitu dengan menyebut nama_fungsi()
nama_fungsi() => cara memanggil isi fungsi aja.

dalam sebuah fungsi sangat diperhatikannya jarak dan white space dan executing flow nya
contoh:
def nama():
    # ini fungsi print didalam fungsi nama
    print("Aku Gentha")
# Sedangkan ini berbeda lagi karena bukan lagi bagian dari fungsi
print("Aku adalah seorang programmer")

Penulisan fungsi di python itu menggunakan def dan menggunakan parameter dan argument nah ini juga kita gunakan multi parameter dan argument
def nama_fungsi(parameter bisa multi):
    # kode yang akan dijalankan => jika kita tidak menuliskan kode di dalam fungsinya maka bisa jadi error
nama_fungsi(argument bisa multi) => argument disini berguna untuk mengisi si parameter fungsi

'''
# Contoh 1
# def nama():
#     print("Aku Gentha")
#     print("Aku adalah seorang programmer")
#     print("Aku bisa menjadi seorang programmer")
# nama()

# Contoh 2 menggunakan parameter dan argument
def nama(nama): # parameter bisa multi bisa jadi (nama1, nama2, nama3)
    print(f"Nama saya adalah {nama}") # ternyata dapat menggunakan format juga ya selain concetenation
nama("Gentha")