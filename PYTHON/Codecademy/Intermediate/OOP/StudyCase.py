# Untuk mengasah kemampuan OOP, ada study casenya yaitu membuat School Catalogue
class School:
    # Dibawah ini adalah Fieldnya dari class School
    def __init__(self, name, level,numberOfStudent):
        # Dibawah ini adalah Constructor dari class School
        self.name = name
        self.level = level
        self.numberOfStudent = numberOfStudent

# Getter
    def getName(self):
        return self.name
    def getLevel(self):
        return self.level
    def getNumber(self):
        return self.numberOfStudent
# Setter (mengganti)
    def setNumber(self, newNumber):
        self.numberOfStudent = newNumber
#Method
    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudent}"
# TEST
mySchool = School("Codecademy", "high", 100)
print(mySchool)
print(mySchool.getName())
print(mySchool.getLevel())
mySchool.setNumber(200) # => Setter kita gunakan setter untuk mengubah nilai 100 yang ada di mySchool
print(mySchool.getNumber())

# Inheritance dari class School
# Create PrimarySchool class
class PrimarySchool(School): #                 ↓↓↓↓↓↓↓↓↓ => Field baru di tambahkan yaitu pickupPolicy
    def __init__(self, name, numberOfStudents, pickupPolicy): 
        # Pada constructor ini kita hanya memerlukan parameter 3 ini tidak termasuk level yang ada di parameter atas
        super().__init__(name, "primary", numberOfStudents)
        # pada pengambilan method dengan super, super().namaMethod(parameter methodnya yang di ambil)
        # disini ada sedikit perubahan yaitu mengubah level menjadi primary(default)
        # jadinya nanti karena kita menggunakan super() dan didalamnya pada bagian level di ganti ganti default
        # berupa "primary"
        # Jadi kaya gini si codenya kalo gk pake super() :
        # self.level = "primary"
        self.pickupPolicy = pickupPolicy

    def getPickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        primarySchool = super().__repr__() # disini kita menyimpan hasil method __repr__ dari super class
        # digunakan untuk nanti menambahkan kalimat lagi.
        return primarySchool + f" The pickup polity is {self.pickupPolicy}"
# TEST PrimarySchool
testSchool = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(testSchool.getPickupPolicy()) 
print(testSchool)

# Create HighSchool Class
class HighSchool(School):
    def __init__(self, name, numberOfStudent, sportTeams):
        # # Pada constructor ini kita hanya memerlukan parameter 3 ini tidak termasuk level yang ada di parameter atas
        super().__init__(name, "High", numberOfStudent)
        # pada pengambilan method dengan super, super().namaMethod(parameter methodnya yang di ambil)
        # disini ada sedikit perubahan yaitu mengubah level menjadi High(default)
        
        self.__sportTeams = sportTeams


    @property
    def getSportTeams(self):
        pass
    @getSportTeams.getter # => Getter kalau semisalnya kita ingin mengambil nilai private dari constractor
    def getSportTeams(self):
        return self.__sportTeams
    
    # Mengganti nilai dari sportTeams
    @getSportTeams.setter
    def getSportTeams(self, newSportTeams):
        self.__sportTeams = newSportTeams
        
    # Jika kita ingin menghapus nilai dari sportTeams kita dapat menggunakan deleter
    @getSportTeams.deleter
    def getSportTeams(self):
        print("Deleting sportTeams")
        self.__sportTeams = None
    # del self.__sportTeams => ini akan error karena kita menggunakan yang namanya property deleter
    
    
    def __repr__(self):
        highSchool = super().__repr__()
        return highSchool + f" Information of our Sport team this school is {self.__sportTeams} "
# TEST HIGHSCHOOL
testHighSchool = HighSchool("SMAN 1 CIBADAK", 400, ["Basket", "Futsal", "Voli"])
print(" ===================== INI GETTER ======================== ")
print(testHighSchool.getSportTeams)
print(testHighSchool)
# Bagaimana jika kita ingin mengganti nilai dari sportTeams?
# Kita gunakan yang namanya itu Setter
# kerennya pake setter penulisan untuk menggantinya seperti variable bukan seperti method tapi variable itu setter.
testHighSchool.getSportTeams = ["Football", "Boling", "Biliard", "Badminton"]
print(" ============== INI SETTER MENGGANTI NILAI SPORTTEAMS ============== ")
print(testHighSchool.getSportTeams)
print(testHighSchool)
# Kita juga bisa menghapus nilai dari sportTeams
print(" ============== INI DELETER ===================== ")
del testHighSchool.getSportTeams
print(testHighSchool.getSportTeams)
print(testHighSchool)






