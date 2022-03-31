# Katakanlah kita memiliki dua daftar yang ingin kita gabungkan ke dalam kamus, seperti daftar siswa dan
# daftar tinggi mereka, dalam inci:

nama = ['Jenny', 'Alexus', 'Sam', 'Grace']
ketinggian = [61, 70, 67, 64]
# Python memungkinkan Anda membuat kamus menggunakan pemahaman dict, dengan sintaks ini:

siswa = {key:value for key, value in zip(nama, ketinggian)}
# siswa sekarang {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
# Ingat bahwa zip() menggabungkan dua daftar menjadi iterator tupel dengan elemen daftar yang dipasangkan
# bersama. Pemahaman dict ini:

# 1. Mengambil pasangan dari iterator tupel
# 2. Beri nama elemen dalam kunci pasangan (yang berasal dari daftar nama) dan nilai (yang berasal dari daftar
# ketinggian)
# 3. Membuat kunci : item nilai dalam kamus siswa
# 4. Ulangi langkah 1-3 untuk seluruh iterator pasangan

# Diatas adalah cara menggunakan dict comprehension.
# Contoh lain: (menggunakan zip)
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine) # zip() mengembalikan iterator tupel menggabungkan dua daftar 

drinks_to_caffeine = {key:value for key, value in zipped_drinks # Kemudia disini dilakukan for each yang gunanya bisa memasukan key:value dari 2 daftar kedalam dict
}


# Review codecademy tentang dict compresion
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key,value in zip(songs, playcounts)
}
print(plays)
plays["Purple Haze"] = 1
plays.update({"Respect":94,})

library = {
    "The Best Songs" : plays, "Sunday Feelings" : {}
}
print(library)
