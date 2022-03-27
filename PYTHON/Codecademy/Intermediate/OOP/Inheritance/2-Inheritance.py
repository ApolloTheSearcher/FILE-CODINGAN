# Multiple Inheritance Part 2
'''
Perbedaan dari yang pertama yaitu bahwa nanti kita pada class Inheritance kita bisa menggunakan lebih dari
satu parameter sesuai jumlah class yang sebelumnya dibuat untuk menggambil data dari setiap classnya
Bentuk lain dari multiple inheritance melibatkan subclass yang mewarisi langsung dari dua kelas dan dapat
menggunakan atribut dan metode keduanya.
Contoh Cases menggunakan Multiple Inheritance:
'''
class Employee():
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}.".format(self.id))

class User:
    def __init__(self, username, role="Customer"):
        self.username = username
        self.role = role

    def say_user_info(self):
        print("My username is {}".format(self.username))
        print("My role is {}".format(self.role))

# Write your code below
class Admin(Employee, User):
    def __init__(self):
        super().__init__() # menggunakan super() untuk mengakses method dari class dari User
        User.__init__(self, self.id, "Admin") # Ini digunakan untuk mengganti isi parameter dari method __init__()
                                                # dari class User
# Jadi cara mengganti parameter pada method yang diambil dari class lain yaitu dengan cara
# => namaClass.namaMethod(self, parameter)

    def say_id(self):
        super().say_id() # menggunakan super() untuk mengakses method dari class dari Employee
        print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()
print("+++++++++++++++++++++++++++++")
e3.say_id()