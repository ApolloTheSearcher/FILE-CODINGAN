# Oke kita lanjut ke pembahasannya selanjutnya yaitu mengenai operasi operasi yang ada di dalam set.
# Yaitu: Onion, Intersection (and Intersection update), Difference (and Difference update), Symmetric Difference (and Symmetric Difference update)
# Onion:
'''
Digunakan untuk menggabungkan dua set. jika kedua data set tersebut berbeda jika semisalnya ada data yang 
sama maka data yang sama akan diabaikan. atau juga kita bisa menggabungkan dua set dengan | operator. fungsinya sama saja
Dan union ini dapat menggabungkan 2 set yaitu set dan frozenset. tetapi kelemahannya dia hanya dapat menggabungkan 
2 set yang berbeda.
Melakukannya akan mengembalikan set baru atau frozenset yang berisi semua elemen dari kedua set tanpa duplikat.
Contoh:
'''
# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}
py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

# Get the union using the .union() method
combined_tags = prepare_to_py.union(py_and_dry)
print(combined_tags)
'''
Outputnya:
{'electric guitar', 'classic', 'heavy metal', 'rock and roll', 'rock', 'synth'}
'''
# Contoh jika menggunakan operasi | operator:
# Get the union using the | operator
frozen_combined_tags = py_and_dry | prepare_to_py
print(frozen_combined_tags)
'''
Outputnya:
frozenset({'electric guitar', 'rock and roll', 'rock', 'synth', 'heavy metal', 'classic'})
karena menggunakan operator | maka frozenset yang akan di tampilkan karena nilai dari py_and_dry
'''
# Contoh lainnya:
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
            'Wait For Limit': ['rap', 'upbeat', 'romance'],
            'Stomping Cue': ['country', 'fiddle', 'party'],
            'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Write your code below!
new_song_data = {}
for key, val in song_data.items():
    song_data_set = set(val)
    user_tag_set = set(user_tag_data[key])
    new_song_data[key] = user_tag_set.union(song_data_set)
print(new_song_data)
'''
Pada baris ke 45 itu kenapa saya key,val sebab karena set dan pada 2 data set di atas mengandung key, value
dan kemudian saya looping ke song_data.items() untuk mengambil key dan value dari song_data.
setelah itu pada baris ke 46 kenapa pada song_data_set itu mengambil value dari song_data.items() karena 
value pada kedua data sama jadi saya ambil salah satu dan di simpan ke dalam set song_data_set.
kemudian pada baris ke 47 mengambil key karena kita mau mengambil key dari salah satu data set yang ada di atas
kemudia pada baris ke 48 itu new_song_data kenapa key karena key menjadi kuncinya utamanya kemudian di gabungkan
union atau bisa juga menggunakan operator |.
'''

# Intersection (and Intersection update):
'''
Digunakan untuk menggabungkan dua set. dan menghasilkan nilai yang duplikat. atau digunakan untuk menghitung
nilai yang sama pada data set. bisa set biasa atau frozenset.
Kita bisa menggunakan .intersection() method atau bisa menggunakan operator &.
'''
# Contoh:
# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

# Find the intersection between them while providing the `frozenset` first.
frozen_intersected_tags = py_and_dry.intersection(prepare_to_py)
print(frozen_intersected_tags)
# OUTPUTNYA: frozenset({'rock', 'classic', 'electric guitar'})
# Contoh jika menggunakan operator &:
# Find the intersection using the operator `&` and providing the normal set first
intersected_tags = prepare_to_py & py_and_dry
print(intersected_tags) # Outputnya: {'rock', 'classic', 'electric guitar'}

# Contoh lainnya:
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
            'Wait For Limit': ['rap', 'upbeat', 'romance'],
            'Stomping Cue': ['country', 'fiddle', 'party'],
            'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
            'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
            'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
            'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
            'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                    'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# Write your code below!
tags_int = set(user_recent_songs['Retro Words']) & set(user_recent_songs['Lowkey Space'])

recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tags_int:
            if key not in user_recent_songs:
                recommended_songs[key] = val

print(recommended_songs)

# Difference (and Difference update):
'''
Untuk melakukannya, set atau frozenset menggunakan metode .difference() atau - operator. 
Ini mengembalikan set atau frozenset, yang hanya berisi elemen dari set pertama yang tidak ditemukan di set 
kedua. Mirip dengan operasi lain, jenis operan pertama (set atau frozenset di sisi kiri operator atau metode)
menentukan apakah set atau frozenset dikembalikan ketika menemukan perbedaannya.
Jadi akan menghasilkan nilai set jika di antara set pertama dan set kedua tidak ada elemen yang sama.
'''
# Contoh .difference():
# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

# Find the elements which are only in prepare_to_py
only_in_prepare_to_py = prepare_to_py.difference(py_and_dry) # # Hasilnya di pengaruhi terhadap apa yang di panggil terlebih dahulu di bagian kiri
# karena pada ony_in_prepare_to_py yang di panggil terlebih dahulu di bagian kiri itu prepare_to_py maka hasilnya nilai pada set prepare_to_py
print(only_in_prepare_to_py) # Outputnya: {'heavy metal', 'synth'}

# Contoh jika menggunakan operator -:
only_in_py_and_dry = py_and_dry - prepare_to_py # Hasilnya di pengaruhi terhadap apa yang di panggil terlebih dahulu di bagian kiri
# karena pada ony_in_py_and_dry yang di panggil terlebih dahulu di bagian kiri itu py_and_dry maka hasilnya nilai pada set py_and_dry
print(only_in_py_and_dry) # Outputnya: {'classic', 'rock and roll'}

# Contoh lainnya:
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                'Stomping Cue': ['country', 'fiddle', 'party'],
                'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
                'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

# Write your code below!
# Check Point 1
tag_diff = set(user_liked_song['Back To Art']) - set(user_disliked_song['Retro Words'])

# Check Point 2
recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tag_diff:
            if key not in user_liked_song and key not in user_disliked_song:
                recommended_songs[key] = val
print(recommended_songs)
'''
<loop through each song in song_data> 
    <loop through each tag in song_data for a specific song>
        <if the tag is inside of tag_diff> 
            <check if the user has not listened to the specific song in user_liked_song or user_disliked_song> 
                <add the song and associated tags to recommended_songs>
'''

# Symmetric Difference (and Symmetric Difference update):
'''
menganggap operasi ini sebagai kebalikan dari Intersection Operation. Himpunan yang dihasilkan akan mencakup semua elemen dari 
himpunan yang berada dalam satu atau yang lain, tetapi tidak keduanya. Dengan kata lain, elemen yang unik untuk setiap himpunan.
Untuk melakukan operasi ini pada wadah set atau frozenset, kita dapat menggunakan metode .symmetric_difference() atau operator ^. 
Seperti operator lain, jenis operan pertama (set atau frozenset di sisi kiri operator atau metode) menentukan apakah set atau 
frozenset dikembalikan ketika menemukan perbedaan simetris.
'''
# Contoh .symmetric_difference():
# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}
py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})
# Find the elements which are exclusive to each song and not shared using the method
exclusive_tags = prepare_to_py.symmetric_difference(py_and_dry)
print(exclusive_tags) # Outputnya: {'heavy metal', 'synth', 'classic', 'rock and roll'}
# Contoh jika menggunakan operator ^:
# Find the elements which are exclusive to each song and not shared using the operator
frozen_exclusive_tags = py_and_dry ^ prepare_to_py
print(frozen_exclusive_tags) # Outputnya: frozenset({'synth', 'rock and roll', 'heavy metal', 'classic'})

# Contoh lainnya:
user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                    'Stomping Cue': ['country', 'fiddle', 'party'],
                    'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                    'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                    'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                    'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                    'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

# Write your code below!
# Checkpoint 1
user_tags = set()
for key, val in user_song_history.items():
    user_tags.update(set(val)) # yang kita ambil hanya value nya saja kemudia akan di tambahkan ke dalam set

# Checkpoint 2
friend_tags = set()
for key, val in friend_song_history.items():
    friend_tags.update(set(val)) # Kita hanya menggunakan metode update() untuk menambahkan elemen ke dalam set yaitu val

# Checkpoint 3
unique_tags = set(user_tags ^ friend_tags)
print(unique_tags)

