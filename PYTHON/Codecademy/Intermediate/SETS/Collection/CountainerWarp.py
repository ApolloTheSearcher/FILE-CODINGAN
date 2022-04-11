# Counter Warp adalah suatu cara yang digunakan untuk sebuah class, atau membungkus sebuah fungsi yang 
# mengembalikan sebuah object, dimana kita untuk Counter Warp kita harus membuat sebuah class baru dan itu 
# menjadi turunan class induknya. tetapi kita juga bisa menggunakannya untuk membungkus fungsi
# seperti kita membuat parameter baru tetapi parameter tersebut tetap berisi parameter dari induknya.
# Contoh program:
class Customer:
    def __init__(self, name, age, address, phone_number):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number

class CustomerWrap(Customer):

    def __init__(self, name, age, address, phone_number):
        self.customer = Customer(name, age, address, phone_number) # disini kita membuat parameter baru yang berisi parameter dari Customer
        # Inheretance dari Customer ke CustomerWrap

    def display_customer_info(self):
        print('Name: ' + self.customer.name) # sehingga di fungsi ini kita memanggilnya dengan menggunakan
        print('Age: ' + str(self.customer.age))# parameter yang berada di dalam class Customer tetapi telah diberi
        print('Address: ' + self.customer.address) # ke parameter baru yang berada di dalam class CustomerWrap
        print('Phone Number: ' + self.customer.phone_number)


customer = CustomerWrap('Dmitri Buyer', 38, '123 Python Avenue', '5557098603')
customer.display_customer_info()

'''
selain itu pada collection terdapat 3 kelas pembungkus berbeda yang disiapkan untuk di modifikasi
Tiga wadah pembungkus yang akan kita lihat adalah:
- UserDict
- UserList
- UserString
'''

# UserDict
# UserDict adalah kelas pembungkus yang menyimpan data dalam bentuk dictionary. kelas ini berisi semua
# Fungsional dict normal, kecuali kita mengakses data dict tdi dalam class dengan menggunakan property
# Contoh programnya :
from collections import UserDict
# Create a class which inherits from the UserDict class
class DisplayDict(UserDict): # mengambil inheritance dari class UserDict di collections
    # A new method to increase the dictionary's functionality
    def display_info(self):
        print("Number of Keys: " + str(len(self.keys()))) # keys ini adalah sebenarnya inheritance dari UserDict
        print("Keys: " + str(list(self.keys())))
        print("Number of Values: " + str(len(self.values()))) # Value juga sama dengan kaya keys
        print("Values: " + str(list(self.values())))

    # We can also overwrite a method from the dictionary class
    def clear(self):
        print("Deleting all items from the dictionary!")
        super().clear() # super() adalah sebuah fungsi yang digunakan untuk mengakses method dari induknya

disp_dict = DisplayDict({'user': 'Mark', 'device': 'desktop', 'num_visits': 37})
disp_dict.display_info()
disp_dict.clear()

# Contoh lain:
from collections import UserDict
data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

# Write your code below!
class OrderProcessingDict(UserDict):
    def clean_orders(self):
        to_del = []
        for key, val in self.data.items():
            if val['order_status'] == 'complete':
                to_del.append(key)
        for items in to_del:
            del  self.data[items]

    def cekCleanOrders(self):
        cek_clean = []
        remove = []
        for key, val in self.data.items():
            if val['order_status'] == 'complete':
                cek_clean.append(key)
            elif val['order_status'] == 'processing':
                remove.append(key)
        for remv in remove:
            del self.data[remv]
        for cek in cek_clean:
            return self.data[cek]

process_dict = OrderProcessingDict(data)
process_dict.clean_orders() 
cekCleandict = OrderProcessingDict(data)
cekCleandict.cekCleanOrders()
print(process_dict)
print("+++++++++++++++++++++++++++++++++++++++++") 
print(cekCleandict)

# UserList
# Userlist adalah sebuah module dari collections yang digunakan sebagai wadah pembungkus atau juga memungkinkan
# kita membuat dict kita sendiri dari List.
# Module ini digunakan pada class sebagai Inheritance dan didalamnya masih bisa menggunakan fungsi fungsi
# yang ada pada list
# Pada UserList ini kita memiliki property yang bernama self.data yang memungkinkan kita untuk mengakses
# list langsung
# Contoh programnya:
from collections import UserList
listangka = [4, 6, 8, 9, 5, 7, 3, 1, 0]

# Write your code below!
class ListSorter(UserList):
    def append(self,items):
        self.data.append(items) # self.data ini kita bisa akses langsung dari data yang ada di list atas
        self.data.sort()

sorted_list = ListSorter(data)
sorted_list.append(2)
print(sorted_list)

# UserString
'''
Karena string juga dianggap sebagai wadah, collectionsmodul juga menyediakan pembungkus wadah untuk kelas
string. Ini berisi semua fungsionalitas string biasa, tetapi ini termasuk data string di dalam properti yang
disebut data. Mewarisi dari kelas ini memungkinkan kita untuk membuat versi string kita sendiri!
'''
# Contoh:
from collections import UserString
# Create a class which inherits from the UserString class
class IntenseString(UserString):
    # A new method to capitalize and add exclamation points to our string
    def exclaim(self):
        self.data = self.data.upper() + '!!!'
        return self.data
    # Overwrite the count method to only count a certain letter
    def count(self, sub=None, start=0, end=0):
        num = 0
        for let in self.data:
            if let == 'P':
                num+=1
        return num
    
intense_string = IntenseString("python rules")

print(intense_string.exclaim())
print(intense_string.count())

# atau contoh lain:
from collections import UserString

str_name = 'python powered patterned products'
str_word = 'patterned '

# Write your code below!
class SubtractString(UserString):
    def __sub__(self, items):
        if items in self.data:
            self.data = self.data.replace(items,'')

subtract_string = SubtractString(str_name)
subtract_string - str_word
print(subtract_string)