# Chain Map
'''
Sebelumnya kita membahas mengenai module dict yang dapat kita gunakan untuk mengurutkan atau memindahkan data
di dalam dict tanpa adanya index atau secara otomatis, selanjutnya terdapat module yang bernama ChainMap.
wadah ChainMap memungkinkan kita untuk menyimpan banyak pemetaan dalam grup terurut, tetapi pencarian
(mengakses nilai menggunakan kunci) diulang untuk setiap pemetaan di dalam ChainMap sampai sesuatu ditemukan atau akhir tercapai. 
Jika kami mencoba mengubah data dengan cara apa pun, maka hanya pemetaan pertama di ChainMap yang akan menerima perubahan. 
Saat mengakses data, salah satu cara untuk memikirkan ChainMap adalah memperlakukan semua kamus yang disimpan sebagai satu kamus besar,
di mana jika ada kunci yang berulang, maka hasil pertama yang ditemukan akan dikembalikan.
Jadi kesimpulannya itu jika kita menggunakan ini untuk menggabungkan banyak dict menjadi satu dict, dan dimana pada ChainMap
terdapat 2 fungsi yang baru kita ketahui yaitu .parent() dan .new_child().
dimana .parent() akan mengembalikan semua isi gabungan dari semua kamus tetapi tidak mengembalikan kamus yang awal.
sedangkan .new_child() akan mengembalikan semua kamus yang di gabungkan menjadi satu.
Contoh program:
'''
from collections import ChainMap
year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# Write your code below!
#Chechpoint 1
profit_map = ChainMap(*year_profit_data) # menggabungkan dict menjadi satu dict dimana * ini menunjukan sebagai individual argument
# bukan sebagai single argument

# Checkpoint 2
def get_profits(input_map):  #karena yang dimasukan ke parameter fungsi adalah input_map, yang mana nanti akan diisi oleh dict
    total_standard_profit = 0 # sehingga kita untuk mencari keynya menggunakan fungsi .keys()
    total_holiday_profit = 0 
    for key in input_map.keys(): # disini melakukan perulangan untuk mencari key yang ada di dalam dict
        if 'holiday' in key: # jika key yang dicari mengandung 'holiday' maka akan dihitung
            total_holiday_profit += input_map[key] # kemudian dijumlahkan dengan total_holiday_profit key yang dicari
        else:
            total_standard_profit += input_map[key] 
    return total_standard_profit, total_holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map) # dimana nanti ada 2 variable ini adalah hasil return
# dari fungsi get_profits

#Checkpoint 3
for item in new_months_data:
    profit_map = profit_map.new_child(item) # disini dia akan mengambil data item tetapi tidak menghitung induknya

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)

#Checkpoint 4
year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit-last_year_holiday_profit
print(year_diff_standard_profit)
print(year_diff_holiday_profit)

# Counter
'''
Sebuah fungsi collections di peruntukan untuk menghitung jumlah kemunculan sebuah nilai pada sebuah list dan kemudian di konvert
menjadi sebuah dict. 
Contoh pengggunannya
'''
# Jika tidak menggunakan Counter, maka kita harus menggunakan looping untuk menghitung jumlah kemunculan sebuah nilai pada sebuah list
clothes_list = ['skirt', 'hoodie', 'dress', 'blouse', 'jeans', 'shoes', 'skirt', 'skirt', 'jeans', 'hoodie', 'boots', 'jeans', 
                'jacket', 't-shirt', 'skirt', 'skirt', 'dress', 'shoes', 'blouse', 'hoodie', 'skirt', 'boots', 'shoes', 'boots', 
                'jeans', 'hoodie', 'blouse', 'hoodie', 'shoes', 'shoes', 'blouse', 'boots', 'blouse', 'hoodie', 't-shirt', 'jeans', 
                'dress', 'skirt', 'jacket', 'boots', 'skirt', 'dress', 'jeans', 'jeans', 'jacket', 'jeans', 'shoes', 'dress', 'hoodie', 
                'blouse']

count_clothes_items = {}
for item in clothes_list:
    if item not in count_clothes_items:
        count_clothes_items[item] = 1
    else:
        count_clothes_items += 1
print(count_clothes_items)

# Contoh jika kita menggunakan module dari collections yaitu fungsi dari Counter
from collections import Counter
count_clothers_items_user = Counter(clothes_list) # Lebih mudah dan gampang kan hehe
print(count_clothers_items_user)

# Contoh lain:
from collections import Counter
opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 
                    'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 
                    'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 
                    'blouse']

# Write your code below!
def find_amount_sold(opening, closing, item):
    opening_count = Counter(opening)
    closing_count = Counter(closing)
    opening_count.subtract(closing_count) # untuk mengurangi closing_count dengan opening_count
    return opening_count[item]

tshirts_sold = find_amount_sold(opening_inventory, closing_inventory, 't-shirt') # untuk mencari t-shirt yang dijual
print(tshirts_sold)

