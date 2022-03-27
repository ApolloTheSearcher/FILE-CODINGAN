# OOP PILLAR : ABSTRACTION
'''
Jadi apabila sebuah program mulai menjadi besar, pada class mungkin akan berbagi fungsionalitas atau kehilangan
tujuan dari struktur Inheritance class. Untuk mengatasi hal seperti ini kita gunakan abstraction.
Abstraksi membantu dengan desain kode dengan mendefinisikan perilaku yang diperlukan untuk diimplementasikan
dalam struktur kelas. Dengan demikian, abstraksi juga membantu menghindari meninggalkan atau tumpang tindih
fungsionalitas kelas karena hierarki kelas menjadi lebih besar.
Jadi tidak akan ada yang namanya itu overriding method jika kita gunakan abstraction.
=> Jangan lupa jika kita ingin menggunakan abstraction, kita harus menghimportnya terlebih dahulu.
from abc import ABC, abstractmethod => ini adalah cara yang kita gunakan untuk mengimport abstraction.

Tetapi kelemahannya kita ingin memanggil method dari class yang sudah ada abstraction. itu akan membuatnya error.
Contoh CASES BIAR LEBIH JELAS :
'''
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod # => ini adalah method yang kita ingin abstract
    def make_noise(self):
        pass
        print("I am an abstract animal")

class Cat(Animal):
    def make_noise(self):
        print("{} says, Meow!".format(self.name))
class Dog(Animal):
    def make_noise(self):
        print("{} says, Woof!".format(self.name))

kitty = Cat("Maisy")
doggy = Dog("Amber")
kitty.make_noise() # "Maisy says, Meow!"
doggy.make_noise() # "Amber says, Woof!"

# Error jika kita menggunakan code dibawah ini :
# an_animal = Animal("Fred") # => ini adalah kita mengimplementasikan method yang sudah diabstract
# an_animal.make_noise() # => Can't instantiate abstract class Animal with abstract methods make_noise
# Secara logika mana mungkin Animal mengeluarkan suara kalau tidak di spesifikasikannya bahwa dia hewan apa?
# Ketika kita semisalnya ingin memanggil hewan dengan Class Animal Kemudian menggunakan Method make_noise yang
# sudah di abstraction maka kita akan mendapatkan error
