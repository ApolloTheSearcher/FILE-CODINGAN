# Encapsulation adalah cara membuat method dan data tersembunyi di dalam objek terkait. 
# Bahasa mencapai ini dengan apa yang disebut pengubah akses seperti:
'''
=> Private (Private hanya dapat diakses dari kode di dalam kelas yang ditetapkan oleh anggota tersebut.)
=> Protected (anggota yang Protected hanya dapat diakses dari kode dalam modul yang sama)
=> Public (Secara umum, Public dapat diakses dari mana saja)
Penulisannya yaitu dengan konvensi umum para developer yang menggunakan Python.
- yaitu untuk Public seperti biasa penulisan contoh => self.name
Dapat diakses dari mana saja, karena dia adalah Public.

- yaitu untuk Protected penulisan diawali dengan satu garis bawah(single underscore) contoh => self._name
Digunakan menunjukan bahwa ini adalah Protected. Mengakses anggota yang dilindungi di luar modul tidak akan
menyebabkan kesalahan, ditambahkan oleh pengembang untuk memberi tahu pengembang lain bahwa mereka harus
berhati-hati saat mengakses anggota ini dengan cara seperti itu.

- yaitu untuk Private penulisan diawali dengan dua garis bawah(double underscore) contoh => self.__name
Ini lebih dari sekedar konvensi di Python karena mekanisme yang disebut name mangling.
Meskipun mereka masih dapat diakses secara publik, tujuan dari mekanisme ini adalah untuk mencegah bentrokan
nama anggota dari setiap kelas pewarisan yang mungkin mendefinisikan anggota dengan nama yang sama.

Ketiga ini berbeda dengan metode dunder karena metode dunder yaitu dua garis bawah di depan dan di belakang
dan diperlakukan berbeda dari anggota pribadi. Satu perbedaan penting adalah bahwa nama metode dunder tidak
rusak.

"JANGAN LUPA UNTUK MENAMBAHKAN SELF YA"
Contoh Case dibawah ini:
'''
class Employee():
    def __init__(self):
        self.id = None # Public
        # Write your code below
        self._id = 2 # Protected
        self.__id = 2 # Private
        

e = Employee()
print(dir(e))