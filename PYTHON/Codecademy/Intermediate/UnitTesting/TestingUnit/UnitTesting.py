# Digunakan untuk pengujian suatu program jika terdapat error.
#   Tujuan pengujian tidak hanya untuk menemukan bug tetapi untuk menemukannya dengan cepat.
# Membiarkan bug tidak ditemukan dan tidak terselesaikan dapat menyebabkan konsekuensi besar di dunia nyata
'''
- Pengujian Manual:
Dengan pengujian manual, orang fisik berinteraksi dengan perangkat lunak seperti halnya pengguna. Faktanya,
kami telah menguji kode kami secara manual setiap kali kami menjalankannya dan mengamati hasilnya!
- Pengujian Otomatis:
Dengan pengujian otomatis, pengujian dilakukan dengan kode. Umumnya, pengujian otomatis lebih cepat dan kurang
rentan terhadap kesalahan manusia.
'''
# Bab 1 assert Statement
'''
Dari pada kita pengejuian secara manual memakan banyak waktu kita dapat melakukan dengan cara pengujian otomatis
dimana Python menyediakan untuk kita mengecekan sederhana secara otomatis. dengan menggunakan Assert Statement.
Pernyataan tegas dapat digunakan untuk menguji bahwa suatu kondisi tertentu.
Jika kondisi tersebut False, AssertionError dimunculkan dengan pesan kesalahan opsional.
Bentuk syntaxnya:
assert <condition>, <optional message>
Contoh Program:
'''
destinations = {
    'BUD': 'Budapest',
    'CMN': 'Casablanca',
    'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'


# Write your code below:
assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!' # => AssertionError


city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)

# Dibawah ini adalah contoh Unit Testing menggunakan assert statement:
def get_nearest_exit(row_number):
    if row_number < 15:
        location = 'front'
    elif row_number < 30:
        location = 'middle'
    else:
        location = 'back'
    return location
# Write your code below:
def test_row_1():
    assert get_nearest_exit(1) == 'front', 'The nearest exit to row 1 is in the front!'
def test_row_20():
    assert get_nearest_exit(20) == 'middle', 'The nearest exit to row 20 is in the middle!'
def test_row_40():
    assert get_nearest_exit(40) == "back", 'The nearest exit to row 40 is in the back!'
get_nearest_exit(1)
get_nearest_exit(20)
get_nearest_exit(40)
