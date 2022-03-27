# Custom User Defined Exception 
# ternyata kita juga dapat melakukan custom user defined exception dengan menggunakan keyword raise.
# Kita implementasikan pada bentuk class ya:
# Write your code below (Checkpoint 1 & 2)
class InventoryError(Exception):
    pass
    def __init__(self, supply):
        self.supply = supply
    def __str__(self):
        return 'Available supply is only ' + str(self.supply)

inventory = {
    'Piano': 3,
    'Lute': 1,
    'Sitar': 2
}

def submit_order(instrument, quantity):
    supply = inventory[instrument]
    # Write your code below (Checkpoint 3)
    if quantity > supply:
        raise InventoryError(supply)
    else:
        inventory[instrument] -= quantity
        print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)
