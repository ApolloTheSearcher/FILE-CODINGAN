# Cara membuat set pada python:
# Set menggunakan tanda kurung kurawal {} dalam prosesnya
# dan set juga digunakan untuk menyimpan data yang unik. dimana dalam satu kasus jika ada yang datanya duplicate
# maka hanya terhitung 1 jika di hasilkan oleh set.
# Contoh penggunannya:
genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

# Write your code below!
survey_genres = set(genre_results) # mengubah sebuah list menjadi set
print(survey_genres)

survey_abbreviated = {genre[0:3] for genre in genre_results} # melakukan set comprehension dengan mengambil 3 huruf pertama dari setiap genre
print(survey_abbreviated)

# Frozen set
'''
Tidak seperti set normal, Anda hanya dapat membuat frozen set menggunakan konstruktornya.
Ingat bahwa menggunakan frozenset berarti Anda tidak dapat memodifikasi elemen di dalamnya.
'''
# Contoh:
top_genres = ['rap', 'rock', 'pop']

# Write your code below!
frozen_top_genres = frozenset(top_genres)
print(frozen_top_genres)
# atau
# Creating a frozenset from a list
frozen_music_genres = frozenset(['country', 'punk', 'rap', 'techno', 'pop', 'latin'])
empty_frozen_music_genres = frozenset()
print(empty_frozen_music_genres)

# ADDING SET
# Seperti pembahasan sebelumnya pada python course beginner kita pernah sekali membahas tentang set dan bagaimana
# cara menambahkan elemen ke dalam set. dan juga mengupdate sebuah element baru ke dalam set.
# dengan menggunakan add() method. => jika satu per satu yang ingin ditambahkan
# Contoh:
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}
user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'
tag_set = set(song_data['Retro Words'])
tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)
song_data = {'Retro Words' : tag_set}
print(song_data)

# dengan menggunakan update() method. => jika Anda ingin menambahkan semua elemen dalam sebuah list ke dalam set.
# Contoh:
# Create a set to hold the song tags
song_tags = {'country', 'folk', 'acoustic'}
# Add more tags using a hashable object (such as a list of elements)
other_tags = ['live', 'blues', 'acoustic']
song_tags.update(other_tags)
print(song_tags)

# Kemudian selain di atas kita perlu ketahui bahwa untuk menghilangkan data yang ada didalam set kita dapat menggunakan remove
# Tetapi selain remove method terdapat spesifik lagi method yang berfungsi sama seperti remove yaitu discard.
# Dimana discard jika kita ingin menghapus data yang tidak ada di dalam set maka dia tidak akan error atau tidak akan KeyError
# Contoh penggunaan remove:
# Given a list of song tags
song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}
# Remove an existing element (Remove data yang ada di dalam set song_tags)
song_tags.remove('folk')
print(song_tags)
# Try removing a non-existent element (Remove data yang tidak ada di dalam set song_tags)
song_tags.remove('fiddle') # => KeyError yang akan terjadi

# Contoh penggunaan discard:
# Given a list of song tags
song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}
# Try removing a existent element but with the discard method
song_tags.discard('guitar') # Meskipun pakai discard bila memang datanya ada maka akan terhapus 
print(song_tags)
# Try removing a non-existent element but with the discard method
song_tags.discard('fiddle') # => tidak akan terjadi KeyError Jika datanya tidak ada di dalam set
print(song_tags)