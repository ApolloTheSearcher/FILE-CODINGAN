# Pada generator ada satu kata kunci yield. yaitu dipergunakan untuk sama seperti return
# jadi mengembalikan nilai hanya saja dengan menggunakan yield. dan keuntungannya kita dapat menggunakannya 
# multiple yield. tidak bisa seperti return yang hanya mengembalikan satu nilai saja
# Contoh menggunakan yield:
def generator_name():
    yield "Budi"
    yield "Anton"
    yield "Sukinem"
    yield "Joko"

for name in generator_name():
    print(name)

# Next and StopIteration pada generator dengan menggunakan sebuah yield
# Jadi kita dapat membuatnya menjadi sebuah iterator dan itu kita ketika sudah melebihi batas ketentuannya maka
# Otomatis dia akan error dan errornya akan bertuliskan StopIteration
# Contoh Program:
student_list = [
    "Angkasa",
    "Peter",
    "Angkasa",
    "Budi",
    "Anton",
]
def generatorNameList():
    for name in student_list:
        if name == "Angkasa":
            yield 500
        else:
            yield name
studentList = iter(generatorNameList())
print(next(studentList))
print(next(studentList))
print(next(studentList))
print(next(studentList))
print(next(studentList))
print(next(studentList)) # => Error stopIteration karena sudah melebihi batasnya.

