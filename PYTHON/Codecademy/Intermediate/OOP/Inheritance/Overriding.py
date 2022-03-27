# OVERRIDING METHOD
# Jadi konsep Overriding method itu menimpah method yang sama, yang sudah ada di class utama kemudian kita tambahkan
# method lagi di class anaknya(Inheritance).
# Contoh:
class Employee():
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}.".format(self.id))

class Admin(Employee):
    # Write your code below
    def say_id(self):
        print("I am an Admin")
# Dibawah ini Object yang dimasukan kedalam variable (instance)
e1 = Employee()
e2 = Employee()
e3 = Admin()

# e2.say_id() # => My id is 2.
# e3.say_id() # => I am an Admin

'''
perbedaan di antara e2 dan e3 yaitu adalah bahwa e2 itu menyimpan class Employee dan e3 menyimpan class Admin
jadi jika class Employee itu method nya adalah My id dan sedangkan class Admin itu method nya adalah I am an Admin
jadi meskipun sama bentuk methodnya kita bisa lihat method itu terletak pada class yang mana
'''
# Super()
'''
Fungsi super() digunakan untuk mengakses method dari class induknya. jadi semisalnya kita method pada anaknya
dan ingin didalam method anaknya berisi method dari induknya kita dapat menggunakan fungsi super() didalam method
anaknya.
Contoh case sama seperti di atas hanya saja pada method say_id() kita menggunakan super() untuk mengakses method
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
    # Write your code below:
        super().say_id() # fungsi super yang digunakan untuk mengakses method dari class induknya
    
        print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()
# My id is 3
# I am an admin.

# Jadi pada case ini kita bisa menghitung id si e3 karena kita menggunakan super(), sedangkan kita kalau tidak
# menggunakan super() kita bisa menghitung id si e3 juga cuma kita melakukan DRY (Dont Repeat Yourself)


