# Container yang selama ini kita pakai meskipun kita tidak menyadarinya
# - List
# list contohnya seperti append, sort, remove.
products = ['t-shirt', 'pants', 'shoes', 'dress', 'blouse'] # List contohnya
products.append('jacket')
products.sort()
products.remove('shoes')

# - Tuples
# Tuples adalah objek yang tidak dapat diubah yang mengelompokkan beberapa elemen menjadi satu.
# Mereka mirip dengan list, kecuali bahwa mereka tidak dapat diubah setelah dibuat
searched_terms = ('clothes', 'phone', 'app', 'purchase', 'clothes', 'store', 'app', 'clothes')
term = searched_terms[2]
num_of_occurrences = searched_terms.count('clothes')

# - Dictionary
# Dictionary adalah grup pasangan key-value yang tidak berurutan
orders = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99}, 
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99}
        }
order_4829_price = orders['order_4829']['price']
order_6184_size = orders['order_4829']['size']
orders['order_4829']['size'] = 'x-large'
num_of_orders = len(orders)

# - Set
# Set adalah grup elemen yang tidak berurutan yang tidak dapat berisi duplikat, elemen tidak dapat dimodifikasi
old_products_set = {'t-shirt', 'pants', 'shoes'}
new_products_set = {'t-shirt', 'pants', 'blouse', 'dress'}
updated_products = new_products_set | old_products_set # Union
removed_products = old_products_set - new_products_set # Difference

# Contoh program menyeluruh:
# Write your code below!
# Checkpoint 1
company_name = "RIA BUSANA"
# Checkpoint 2
company_location = (2.0, 3.5)
# Checkpoint 3
company_products = ["Baju Spiderman", "Baju Kokoh", "Baju FreeFire", "Baju MobileLegend", "Baju Bola"]
# Checkpoint 4
company_data = {'name':company_name, 'location':company_location, 'products': company_products}
# Cek
print(company_data['name']) # RIA BUSANA