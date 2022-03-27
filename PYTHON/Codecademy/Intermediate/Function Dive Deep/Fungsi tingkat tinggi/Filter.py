# Filter()
'''
Digunakan untuk menyaring data dari sebuah iterable / array juga bisa
Jadi filter itu menghasilkanya True atau False dari data array ketika fungsi yang dimasukan ke dalam filter
itu menghasilkan True atau False
atau tujuan ini dengan menerapkan fungsi pemfilteran yang diteruskan ke setiap elemen dalam iterabel yang
diteruskan
fungsi filter(), fungsi yang mengembalikan nilai boolean True atau False.
Objek filter yang dikembalikan hanya akan menampung elemen-elemen dari iterable yang diteruskan yang fungsi
filternya Dikembalikan True
Penulisan filter() => nama_variable = filter(function, iterable) => functionya bisa berupa lambda
Contoh case menggunakan filter dengan mencari mana yang didalam array terdapat buku hanya judul saja tidak
termasuk tanggalnya atau bisa kita sebut bahwa didalam arraynya harus berupa string saja.
'''
# Jika tidak menggunakan Lambda
books = [["Burgess", 1985],
    ["Orwell", "Nineteen Eighty-four"],
    ["Murakami", "1Q85"],
    ["Orwell", 1984],
    ["Burgess", "Nineteen Eighty-five"],
    ["Murakami", 1985]]
# Your code below: 
def value(x):
    return type(x[1]) == str
    
# Jika menggunakan lambda
string_titles_lambda = filter(lambda x: type(x[1]) == str, books)
# x disitu pada lambda adalah parameter ya bukan nama fungsi
        

# assign the result of your filter function to the variable  string_titles
string_titles = filter(value, books)
# convert your filter object to a list stored in the variable string_titles_list
string_titles_list = list(string_titles)
# print the list string_titles_list
print(string_titles_list)
# jika menggunakan lambda
print(list(string_titles_lambda))



