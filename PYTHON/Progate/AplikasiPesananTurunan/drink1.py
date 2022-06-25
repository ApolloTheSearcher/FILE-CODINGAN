from menu_item2 import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price, volume):
        super().__init__(name, price) # super() digunakan untuk menimpa method init supaya tidak nulis ulang lagi
        self.volume = volume

    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.volume) + 'mL)'
