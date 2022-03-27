# Jadi untuk property kita bisa menggunakan @property dan pada property decorator juga terdapat yang namanya
# Getter, Setter, Deleter digunakan untuk mengakses nilai private dari constructor
class School:
    def __init__(self, name, level,numberOfStudent):
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

# Create PrimarySchool class
class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy): 
        # Pada constructor ini kita hanya memerlukan parameter 3 ini tidak termasuk level yang ada di parameter atas
        super().__init__(name, "primary", numberOfStudents)
        # pada pengambilan method dengan super, super().namaMethod(parameter methodnya yang di ambil)
        # disini ada sedikit perubahan yaitu mengubah level menjadi primary(default)
        self.__pickupPolicy = pickupPolicy # private variable kita ubah untuk bisa nanti pakai property getter dan setter
    @property
    def getPickupPolicy(self):
        pass
    @getPickupPolicy.getter
    def getPickupPolicy(self):
        return self.__pickupPolicy
    @getPickupPolicy.setter
    def getPickupPolicy(self, newPolicy): # untuk setter pada parameter terdapat argument untuk menginput
        self.__pickupPolicy = newPolicy
        info1 = print(self.__pickupPolicy, f"\nPickup telah diganti menjadi {self.__pickupPolicy}")
        return info1
    @getPickupPolicy.deleter
    def getPickupPolicy(self):
        print("Ini telah di hapus sehingga menjadi None")
        self.__pickupPolicy = None
        info2 = f"Pickup Policy telah di hapus {self.__pickupPolicy}"
        return info2

    def __repr__(self):
        primarySchool = super().__repr__() # disini kita menyimpan hasil method __repr__ dari super class
        # digunakan untuk nanti menambahkan kalimat lagi.
        return primarySchool + f" The pickup polity is {self.__pickupPolicy}"
# TEST PrimarySchool
testSchool = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print("==== INI GETTER PRIMARY SCHOOL ====")
print(testSchool.getPickupPolicy)
print(testSchool)
print("==== INI SETTER PRIMARY SCHOOL ====")
testSchool.getPickupPolicy = "Pickup Not Allowed"
testSchool.getPickupPolicy
print(testSchool)
print("==== INI DELETER PRIMARY SCHOOL ====")
del testSchool.getPickupPolicy
print(testSchool.getPickupPolicy)
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
print(" ============== INI SETTER MENGGANTI NILAI SPORTTEAMS ============== ")
testHighSchool.getSportTeams = ["Football", "Boling", "Biliard", "Badminton"]
print(testHighSchool.getSportTeams)
print(testHighSchool)
# Kita juga bisa menghapus nilai dari sportTeams
print(" ============== INI DELETER ===================== ")
del testHighSchool.getSportTeams
print(testHighSchool.getSportTeams)
print(testHighSchool)
