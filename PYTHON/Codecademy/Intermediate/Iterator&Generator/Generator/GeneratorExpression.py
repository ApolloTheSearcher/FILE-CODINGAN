# Generator Expression memungkinkan definisi satu baris yang bersih dan pembuatan iterator. 
# Dengan menggunakan ekspresi generator, tidak perlu mendefinisikan fungsi generator penuh seperti yang telah 
# kita bahas pada latihan sebelumnya.
# Jadi kita bisa tanpa fungsi generator penuh kita cukup mungkin fungsi generator yang isinya hanya perulangan
# Nah untuk generator expression hampir sama syntax nya dengan comparasion list. hanya ada beberapa perbedaan:
# Generator Expression : ngereturn iterator yang baru ditentukan, menggunakan tanda kurung buka dan kurung tutup
# List Comprehension : ngereturn list yang baru, menggunakan tanda kurung siku.
# Contoh:
generator_Expression = (i*i for i in range(10)) # => Generator Expression
list_comprehension = [i*i for i in range(4)] # => List Comprehension
print(generator_Expression) # => <generator object <genexpr> at 0x7f8b8d8b0e10> kenapa karena yang tadi dijelaskan
# Bahwa generator expression menghasilkan iterator yang baru ditentukan. nah untuk mengeluarkan nilainya kita dapat
# menggunakan looping menjadi seperti ini:
for generate in generator_Expression:
    print(generate)
    '''
    0, 1, 4, 9, 16, 25, 36, 49, 64, 81 # => Hasilnya
    '''
# Contoh lainnya yaitu:
def cs_generator():
    for i in range(1,5):
        yield "Computer Science " + str(i)

# Write your code below:
cs_courses = cs_generator()
for course in cs_courses:
    print(course)

cs_generator_exp = ("Computer Science {}".format(i) for i in range(1,5)) # => Generator Expression yang baru

for i in cs_generator_exp:
    print(i) # => Digunakan untuk menghasilkan dari iterator cs_generator_exp.


