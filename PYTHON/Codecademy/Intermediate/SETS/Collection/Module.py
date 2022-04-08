# Pembahasan mendalam mengenai module module yang ada pada collections.
'''
Class dari modul collections sangat mirip dengan wadah bawaan yang telah kita gunakan, tetapi berisi metode dan
utilitas baru. Masing-masing wadah khusus ini berfokus pada peningkatan tertentu pada mitra bawaannya seperti
mengoptimalkan kinerja, organisasi yang lebih baik, langkah yang lebih sedikit untuk melakukan tugas, dan
banyak lagi!
# Contoh import yang dapat kalian gunakan ketika ingin menggunakan module collections
# To import a single class or multiple classes
from collections import name_of_class, name_of_another_class

# To import all classes in the collections module
from collections import *

# Another way to import all classes in a module
import collections

kita juga dapat mengimport sebuah container dari collections yaitu collectionnya sebagai berikut;
Advanced Containers

- Advance Containers:
deque
namedtuple
Counter
defaultdict
OrderedDict
ChainMap
Container Wrappers

- Container Wrappers:
UserDict
UserList
UserString
'''
# Contoh programnya:
from collections import OrderedDict

orders = OrderedDict({'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}})

orders.move_to_end('order_4829')
orders.popitem()
print(orders)