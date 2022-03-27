# Dunder Method
'''
Kode di bawah ini menunjukkan bahwa ketika bekerja dengan jenis objek yang berbeda seperti, int, str atau
daftar, operator + melakukan fungsi yang berbeda. Ini dikenal sebagai operator overloading dan merupakan
bentuk lain dari polimorfisme.
Untuk menerapkan perilaku ini, pertama-tama kita harus membahas metode dunder. Setiap kelas yang ditentukan
dalam Python memiliki akses ke grup metode khusus ini. Kami telah menjelajahi beberapa, konstruktor __init__()
dan metode representasi string __repr__().
Ingat bahwa metode __repr__() hanya membutuhkan satu parameter, self, dan harus mengembalikan nilai string
Dan metode __init__() bisa membutuhkan self , dan parameter lainnya. atau hanya self saja juga bisa
Kemudian untuk Dunder Method __add__() berisi self dan satu parameter untuk berfungsi operator +
Contoh Case dibawah ini:
'''
class Employee():
    new_id = 1 
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

class Meeting:
    def __init__(self):
        self.attendees = []
        
    # Dibawah ini adalah DunderMethod
    def __add__(self, employee):
        print("ID {} added.".format(employee.id)) 
        self.attendees.append(employee)

# Write your code
    def __len__(self):
        return len(self.attendees)

e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
# Dibawah ini adalah proses yang digunakan untuk mengaktifkan DunderMethod
m1 + e1
m1 + e2
m1 + e3
####################
print(len(m1))