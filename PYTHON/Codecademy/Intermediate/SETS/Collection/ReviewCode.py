from collections import deque, namedtuple

overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]

# Write your code below!
# Checkpoint 1
split_prices = deque()
# Checkpoint 2
for items in overstock_items:
    if items[1] > 20.00:
        split_prices.appendleft(items)
    else:
        split_prices.append(items)

# Checkpoint 3
ClothesBundle = namedtuple('field_names',['bundle_items', 'bundle_price'])

# Checkpoint 4
bundles = []
while len(split_prices) >= 5:
    bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(), split_prices.popleft()]
    calc_price = sum(b[1] for b in bundle_list)
    bundles.append(ClothesBundle(bundle_list, calc_price))

# Checkpoint 5
promoted_bundles = []
for bundle in bundles:
    if bundle.bundle_price > 100.00: # bundle_price ini berasal dari sum(b[1] for b in calc_price karena dia
        promoted_bundles.append(bundle)# masuk ke ClothesBundle
# Checkpoint 6
print(promoted_bundles)

