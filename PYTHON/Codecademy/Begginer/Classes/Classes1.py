class Rumah:
    # Kalau kita mengisi sebuah data atau function di atas constructor maka akan masuknya kedalam static method, dan static field
    
    
    
    def __init__(self, namaRumah): # Constructor dari class Rumah dan kalau kita mengisi parameternya itu bisa disebut sebagai field
        self.namaRumah = namaRumah # Cara kerja sebuah constructor adalah dengan mengisi fieldnya dengan parameter yang diberikan
    # Dibawah ini adalah sebuah method kita bisa membedakan antara method biasa dan static method yaitu pada parameternya
    # Jika method biasa dia terdapat self.
    def cetakRumah(self):
        print(f"Nama Rumah : {self.namaRumah}")
        
# Contoh class lain yang membahas self 
class SearchEngineEntry:
    secure_prefix = "https://" # ini adalah static field
    def __init__(self, url): # Constructor dari class SearchEngineEntry
        self.url = url

    def secure(self): # Method secure dari class SearchEngineEntry
        # return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
        return f"{SearchEngineEntry.secure_prefix}{self.url}"
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
print(codecademy.secure())
# prints "https://www.codecademy.com"
print(wikipedia.secure())
# prints "https://www.wikipedia.org"

# Contoh class lain yang membahas self
class Circle:
    pi = 3.14 # ini adalah static field
    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
        self.radius = diameter / 2
    def circumference (self):
        return 2 * self.pi * self.radius 
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())





if __name__ == "__main__": # Fungsi main digunakan untuk memanggil sebuah class
    medium_pizza = Circle(12)
    print(medium_pizza.circumference())
