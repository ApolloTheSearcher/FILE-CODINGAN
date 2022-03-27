# Getter Setter Deleter
'''
Menggunakan fungsi Getter, Setter, dan Deleter adalah salah satu cara untuk mengimplementasikan
enkapsulasi dalam Python di mana status atribut kelas dapat ditangani di dalam kelas. Fungsi-fungsi ini
berguna dalam memastikan bahwa data yang ditangani sesuai untuk fungsionalitas kelas yang ditentukan.
=> Getter biasanya pada method kelas yaitu ada tandanya return(mengembalikan()
=> Setter (penyetel) seperti method pada umumnya yaitu lengkap dengan (self,parameter) dan melakukan proses
pada umumnya method biasa
=> Deleter adalah untuk menghapus atribut yang ditangani pada methodnya terdapat fungsi del (yang ingin didelet)

Contoh case dibawah ini:
'''
class Employee():
    new_id = 1
    def __init__(self, name=None):
        self.id = Employee.new_id
        Employee.new_id += 1
        self._name = name

# Write your code below
    def get_name(self): # => Getter
        return self._name # return self._name(Protected)
    def set_name(self, nama): # => Setter
        self._name = nama
    def del_name(self): # => Deleter
        del self._name # del self._name(Protected) => digunakan untuk mengapus name

e1 = Employee("Maisy")
e2 = Employee()



e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name()) # => Method Getter

e2.set_name("Fluffy") # => Method Setter
print(e2.get_name())

e2.del_name() # => Method Deleter
print(e2.get_name()) # => Error kenapa?, karena kita disitu menprint name yang sudah dihapus jadi tidak bakal ada
