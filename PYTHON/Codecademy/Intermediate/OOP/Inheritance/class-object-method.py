'''
OOP ( ORIENTED OBJECT PROGRAMMING )
python is an object oriented programming language
artinya program yang beruorientasi objek
ada yang namnnya class ,object, method
Class harus diisi ya tidak boleh dikosongkan
Kemudian kita juga dalam suatu workspace kita dapat mengisi dengan lebih dari Class Induk
'''
# Class (cara membuat class contoh dibawah ini)
class Kelas:
    
    # Field
    def __init__(self, nama:str, kelas:int ): # => jika ingin menambahkan type data di variablenya (namaVariable:typeData)
        # Constructor.
        self.nama = nama
        self.romble = kelas
    @classmethod # => classmethod karena ada self di parameternya
    def namaSiswa(self): 
        return f"Nama Siswa : {self.nama}"
    @staticmethod # => static method karena tidak ada self di paramaternya
    def namaKelas():
        return "dari kelas : RPL"
        


if __name__ == "__main__":
    Kelas12 = Kelas("Robby", 12) # => ini disebut object (intance)
    print(Kelas12.namaSiswa())
