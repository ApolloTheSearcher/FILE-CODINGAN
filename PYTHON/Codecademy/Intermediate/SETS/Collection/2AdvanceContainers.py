# Advence Containers selanjutnya yang akan kita bahas adalah defaultdict
'''
defaultdict digunakan untuk memberikan nilai default pada key yang tidak ada. jadi jika pada dict
itu tidak terdapat key yang kita inginkan maka akan menghasilkan error. nah dengan menggunakan defaultdict
memberi opsi kembali dengan menambahkan keterangan jika key pada dict tidak ada.
Contoh penggunaan defaultdict:
'''
from collections import defaultdict
site_locations = {'t-shirt': 'Shirts',
                'dress shirt': 'Shirts',
                'flannel shirt': 'Shirts',
                'sweatshirt': 'Shirts',
                'jeans': 'Pants',
                'dress pants': 'Pants',
                'cropped pants': 'Pants',
                'leggings': 'Pants'
                }
updated_products = ['draped blouse', 'leggings', 
                    'undershirt', 'dress shirt', 'jeans', 'sun dress', 
                    'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
# Checkpoint 1
validated_locations = defaultdict(lambda: 'TODO: Add to website') # Ini diberikan value defaultnya ketika terjadi jika key tidak ada

# Checkpoint 2
validated_locations.update(site_locations)
for item in updated_products:
    site_locations[item] = validated_locations[item] # 
print(site_locations)

# Ordered Dict
'''
Pada kasus dict biasanya untuk melacak isi dari dict itu kita harus mencarinya menggunakan indeksnya, 
dan ketika kita menyimpan dict pada daftar, urutannya dipertahankan tetapi kita harus mengakses elemen berdasarkan
indeks sebelumnya sehingga kita dapat mengakses kamus tersebut.
Tetapi bagaimana jika dict yang kita simpan pada daftar yang sangat besar itu tentu sangat menyulitkan, untuk itu
pada module collections kita dapat menggunakan ordered dict. 
'''
from collections import OrderedDict

# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
            ['Order: 2', 'purchased'],
            ['Order: 3', 'purchased'],
            ['Order: 4', 'returned'],
            ['Order: 5', 'purchased'],
            ['Order: 6', 'canceled'],
            ['Order: 7', 'returned'],
            ['Order: 8', 'purchased'],
            ['Order: 9', 'returned'],
            ['Order: 10', 'canceled'],
            ['Order: 11', 'purchased'],
            ['Order: 12', 'returned'],
            ['Order: 13', 'purchased'],
            ['Order: 14', 'canceled'],
            ['Order: 15', 'purchased']]

# Write your code below!
# Checkpoint 1
orders = OrderedDict(order_data)

# Checkpoint 2
to_move = []
to_remove = []
for key, val in orders.items():
    if val == 'returned':
        to_move.append(key)
    elif val == 'canceled':
        to_remove.append(key)
# pada checkpoint 2 ini kita terjadi pemfilteran dimana dibagi menjadi 2 bagian, yaitu yang dihapus dan yang di move dari list order_data
# karena pada list order_data sudah kita ubah menjadi dict, maka otomatis pada 66 kita gunakan perulangan untuk dict
# jika data itu tidak memenuhi syarat kedua di atas maka dia akan di kembalikan ke dict order_data yang telah di ubah menjadi orders
# Checkpoint 3
for item in to_remove: # pada checkpoint 3 ini kita menghapus item yang di canceled dan disimpan pada list to_remove
    orders.pop(item) # atau lebih tepatnya dihapus itemnya dari dict

# Checkpoint 4
for item in to_move:
    orders.move_to_end(item) # proses ini kemudian di pindah dan di urutkan dari awal ke akhir dan kemudian di
print(orders) # lempar ke dalam dict orders yang telh di ubah menjadi ordered dict
# Sedangkan pada checkpoint 4 ini dia mengatur penempatan data yang ada di list to_move untuk di pindahkan ke belakang
# karena data yang ada pada orders yang tidak masuk ke pemfilteran berada di depan.


