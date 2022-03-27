# Dalam penulisan argument pada parameter fungsi kita dapat menggunakan tanda (*) untuk mengambil semua argumen nya
# dan bebas bentuk typedatanya loh
# Contoh:
def print_all(*args):
    print(args)
# Kita panggil:
print_all("String", 120, True, [1, 2, 3], {"a": 1, "b": 2}, (1, 2, 3))
# Bentuk penulisannya:
'''
def name_function(*randomname):
    proces
'''
# Working dengan *args:
# Disini kita dapat menggunakan *args untuk mengambil semua argumen yang ada pada fungsi.
# Kita bisa menggunakan dengan banyak proses dan kondisi loh yang akan digunakan disini akan pakai forEach
# Contoh:
tables = {
    1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}
print(tables)

def assign_table(table_number, name, vip_status=False): 
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = ''

# Write your code below: 
def assign_and_print_order(table_number, *order_items):
    tables[table_number]['order'] = order_items
    for order in order_items:
        print(order)
# New Customer
assign_table(2, 'Arwa', True)

# OrderItems
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')
print(tables)

# Kemudian setelah *arga ada juga cara penulisan argument pada parameter fungsi dengan menggunakan **kwargs
# Perbedaanya kalau *args(bebas namanya tidak args juga) itu pemanggilannya menggunakan Positional Argument saja
# Sedangkan **kwargs(bebas namanya tidak kwargs juga) itu pemanggilannya menggunakan Keyword Argument saja
# Contoh CASE:
tables = {
    1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
        'drinks': 'Orange Juice, Apple Juice',
        'food_items': 'Pancakes'
    }
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}
print(tables)


# Checkpoint2 
def assign_food_items(**order_items):
    print(order_items)
    # Checkpoint 3
    food = order_items.get('food') # get() untuk mengambil value dari key food kita bisa menggunakan fungsi lainnya juga
    drinks = order_items.get('drinks')
    # Checkpoint 4
    print(food)
    print(drinks)
#Checkpoint 5
#Exampla
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')

# Selain itu **kwargs juga bisa kita gunakan for Each juga loh
# Contoh:
tables = {
    1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
        'drinks': 'Orange Juice, Apple Juice',
        'food_items': 'Pancakes'
    }
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}

def assign_table(table_number, name, vip_status=False): 
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = {}

assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)

# Checkpoint 2
def assign_food_items(table_number, **order_items):
    food = order_items.get('food')
    drinks = order_items.get('drinks')
    tables[table_number]['order']['food_items'] = food
    tables[table_number]['order']['drinks'] = drinks

print('\n --- tables after update --- \n')

# Checkpoint 3
assign_food_items(2, food = 'Seabass, Gnocchi, Pizza', drinks = 'Margarita, Water')
print(tables)

# ternyata kita juga bisa menggabungkan kedua seperti contoh berikut:
# Write your code below: 
def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
# Checkpoint2
    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)

#Checkpoint3
single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops', sides = "Mashed Potatoes",
                        dessert_scoops1 = 'Vanilla', dessert_scoops2 = 'Cookies and Cream' )
