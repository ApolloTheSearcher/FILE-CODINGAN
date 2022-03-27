# Inheritance ( penurunan sifat dari class )
'''
Jadi setiap bahasa OOP pasti ada yang namanya incheritance dimana dia akan mewariskan sifat dari class induknya
semisalnya pada induknya class Orang terdapat method makan dan tidur nah ketika kita bikin class baru dan
akan mewariskan sifat dari class Orang tersebut kita dapat memanggil method makan dan tidur dari class Orang
atau mengambil data darinya. sehingga tidak ada penulisan ulang method dan data yang sama.
karena prinsip programming itu DRy (Dont Repeat Yourself) jadi sebisa mungkin jangan sampai DRY
Penulisan inheritance:
class Induk:
    // code (method,object, dll)
class Anak(Induk):
    // code (method,object, dll)
Dibawah adalah contoh case menggunakan Inheritance sederhana:
'''
class Employee():
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}.".format(self.id))
class Admin(Employee):
    pass  

# Write your code below
e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()

# Multiple Inheritance Part 1
'''
Jadi kita dapat menggunakan Inheritance lebih dari satu kali, seperti contoh di bawah ini 
'''
class Employee():
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}.".format(self.id))

class Admin(Employee):
    def say_id(self):
        super().say_id() # fungsi super yang digunakan untuk mengakses method dari class induknya yaitu Employee
        print("I am an admin.")
# Write your code below
class Manager(Admin):
    def say_id(self):
        super().say_id() # fungsi super yang digunakan untuk mengakses method dari class anak pertama yaitu Admin
        print("I am an Manager")


e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
e4.say_id()
# Output:
# My id is 4.
# I am an admin.
# I am an Manager
'''
Method dari setiap class keluar semua karena memang mereka di panggil secara berurutan.
'''


'''
LANJUTAN UNTUK INHERITANCE PART 2 DI FILE 2INHERITANCE.PY
'''

