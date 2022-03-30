'''
Iterables adalah kumpulan objek yang dapat di iterasi(pelajari kembali) memalui proses looping yang nanti proses
itu disebut dengan proses iteration. menggunakan iterables untuk melakukan proses iterasi dan itu adalah tulang
punggung bagaimana kami melakukan operasi yang konsisten pada kumpulan data.
Meskipun baru terdengar baru padahal kita sering menggunakan iterables, seperti list, tuple, dict, set.
Contoh:
dog_foods = {
    "Great Dane Foods" : 4,
    "Min Pip Pup Foods" : 10,  # => dog_foods dalam bentuk dict disebut iterable
    "Pawsome Foods" : 2
}
for food_brand in dog_foods:  # => looping disebutnya iteration
    print(food_brand)
# Hasil dari proses ini ada yang nanti disebut:
iter() # => mengembalikan object iteration (melakukan proses pengecekannya)
next() # => menampilkan nilai dari iteration jika bernilai True pada proses pengecekannya
StopIteration # => memberhentik menampilkan nilai dari iteration jika bernilai False pada proses pengecekannya

Contoh program:
'''
dog_foods = {
    "Great Dane Foods": 4,
    "Min Pip Pup Foods": 10,
    "Pawsome Pup Foods": 8
}

# Write your code below:
dog_food_iterator = iter(dog_foods) # Kita harus membuat si dict dog_food dengan iter kemudian kita dapat
                                    # menggunakan next() atau  .__next__()

next_dog_food1 = next(dog_food_iterator)
print(next_dog_food1) # => "Great Dane Foods"
next_dog_food2 = dog_food_iterator.__next__() # Kita dapat menggunakan setelah pada garis 31 terjadi iter()
next_dog_food3 = dog_food_iterator.__next__()
print(next_dog_food2) # => "Min Pip Pup Foods"
print(next_dog_food3) # => "Pawsome Pup Foods"

for food_name in dog_foods:
    print(food_name)
    '''
    Outputnya:
    Great Dane Foods
    Min Pip Pup Foods
    Pawsome Pup Foods
    '''
next(dog_food_iterator) # => StopIteration Error karena dia sudah mencapai batas akhir


