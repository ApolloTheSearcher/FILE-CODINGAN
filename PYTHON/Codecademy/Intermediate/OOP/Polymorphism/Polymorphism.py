# OOP Pilar Polymorphism
# Dalam pemrograman komputer, polimorfisme adalah kemampuan untuk menerapkan operasi yang identik ke berbagai
# jenis objek. Ini dapat berguna ketika jenis objek mungkin tidak diketahui pada waktu program. Polimorfisme
# dapat diterapkan menggunakan Python dalam berbagai cara. Salah satu contoh yaitu dengan menggunakan array
# jadi nanti semua class utama dan class anaknya kita simpan kedalam array. kemudian kita keluarkan dengan
# for each kemudian pada for Each kita tambahan methodnya 
# Contoh cases:
class Employee():
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}.".format(self.id))

class Admin(Employee):
    def say_id(self):
        super().say_id()
        print("I am an admin.")

class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I am in charge!")

# Write your code below
meeting = [Employee(), Admin(), Manager()]
for startup in meeting:
    startup.say_id()
'''
Outputnya:
My id is 1. => Employee
------------
My id is 2. => Admin
I am an admin.
------------
My id is 3. => Manager
I am an admin.
I am in charge!

Output ini melakukan overriding method
'''
