# Decorators with functions
def namaJabatan(print_name_orang):
    def print_name():
        nama = print_name_orang
        print(nama)
    return print_name

def namaOrangdanJabatan(nama, jabatan):
    return f"Nama {nama} jabatannya sebagai {jabatan}"
    
# Jika kita tidak menggunakan decorator maka kita harus menuliskan fungsi tersebut dan menyimpannya pada
# variable contoh:
# Joko sebagai nama orang dan CEO adalah jabatannya
lengkap_semua = namaJabatan(namaOrangdanJabatan("Joko", "CEO"))
# ini tanpa dekorator diatas
lengkap_semua()

# Dibawah adalah contoh program menggunakan decorator
# Decorator menggunakan tanda @
def namaJabatan(print_name_orang):
    def print_name(*args,**kwargs): # kalau ini parameter fungsi ini dikosongkan maka error maka kita harus menarik
        #sintaknya dengan menggunaka *args dan **kwargs
        # sehingga nanti menjadi def print_name(*args, **kwargs):
        nama = print_name_orang(*args, **kwargs)
        print(nama)
    return print_name

@namaJabatan
def namaOrangdanJabatan(nama, jabatan):
    return f"Nama {nama} jabatannya sebagai {jabatan}"
    
# Jika kita tidak menggunakan decorator maka kita harus menuliskan fungsi tersebut dan menyimpannya pada
# variable contoh:
# Joko sebagai nama orang dan CEO adalah jabatannya
# ini dekorator diatas:
namaOrangdanJabatan("Joko", "CEO")

