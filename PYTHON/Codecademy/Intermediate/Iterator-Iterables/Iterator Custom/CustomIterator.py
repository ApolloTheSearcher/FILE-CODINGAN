# Sebelumnya pada file iterator.py kita menggunakan iterable pada list, tuple, dict, set. bagaimana kalau di
# gunakan pada class sebagai method? kita dapat menggunakannya sebagai method itu disebutnya custom iterator.
# Contoh Program:
class CustomerCounter:
# Write your code below:
    def __iter__(self):
        self.count = 0
        return self
    def __next__(self):
        self.count += 1
        if self.count > 100: # Supaya tidak terjadi infinite looping
            raise StopIteration
        return self.count

customer_counter = CustomerCounter()
for count in customer_counter:
    print(count)

# Contoh program lain:
class FishInventory:
    def __init__(self, fishList):
        self.available_fish = fishList

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.available_fish):
            fish_status = self.available_fish[self.index] + " is available!"
            self.index += 1
            return fish_status
        else:
            raise StopIteration
Fishcount = FishInventory(["salmon", "trout", "pike", "carp", "catfish"])
print(Fishcount)