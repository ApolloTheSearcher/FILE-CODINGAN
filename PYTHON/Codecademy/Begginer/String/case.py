# program di bawah di gunakan untuk menambahkan suatu huruf yang sama pada dua input yang berbeda
def contains(big_string, little_string):
    return little_string in big_string

def common_letters(string_one, string_two):
    listl = []
    for letter in string_one:
        if(letter in string_two) and not(letter in listl):
            listl.append(letter)
    return listl

print(common_letters("Gentha", "Ardaana"))

# program di bawah tentang membuat username yang apabila di input1 jumlah hurufnya < 3 maka yang dimasukan semua huruf yang ada di input1
# input1 jumlah huruf < 4 maka yang dimasukan semua huruf yang ada di input2 , tetapi jika kedua input memenuhi syarat maka yang dimasukan adalah
# untuk input1 yaitu 4 huruf terakhir dari input1 dan input2 4 huruf awal dari input2
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
username = username_generator("Abe", "Simpson")


def password_generator(username):
    password = ""
    for i in range(0,len(username)):
        password += username[i-1]
    return password

print(password_generator(username))
# Outputnya
# pAbeSim

# Pada string itu ada yang namanya find sama slice
# jadi kalau slice itu pakenya [awal:akhir]
# sedangkan kalau find itu pakenya [yang dicari]
# contoh :
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2] # => INI FIND
final_word = company_motto[-4:] # => INI SLICE