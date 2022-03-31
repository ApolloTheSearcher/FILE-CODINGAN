# Jika kita ingin mengganti sebuah karakter dalam sebuah string dengan menggunakan slice dan concetenation
# yaitu dengan menggunakan
first_name = "Gentha"
fixed_name = "R" + first_name[1:] # => INI CONCETENATION (SLICE + CONCETENATION) konsepnya itu kan itu R dan pada first_name[1:] dimulai dari index 1 berati yang di ganti itu index 0
print(fixed_name)

# Escape character
# Jika kita menemukan sebuah character pada sebuah tanda" " maka kita harus menggunakan escape character ketika ingin menggunakannya
# Contoh

#password = "theycallme"crazy"91" # Error kemudian di ubah menjadikan password = "theycallme\"crazy\"91"

password = "theycallme\"crazy\"91"


# Contoh jika kita ingin menggunakan fungsi strip namun variable data nya beberbentuk list
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', 
                    '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip()) # => INI STRIP dipake untuk mengatasinya pake for loop
print(love_maybe_lines_stripped)

love_maybe_full = "\n".join(love_maybe_lines_stripped) # => INI JOIN supaya menambahkan garis baru disetiap kalimatnya
print(love_maybe_full)

# FUNGSI REPLACE
# Cara penulisannya yaitu dengan menggunakan .replace(old yang ingin di ganti, new yang menjadi pengganti old)
# Contoh:
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington,
D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham
County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life
of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

# Fungsi Find
# digunakan untuk mencari karakter yang ingin dicari dan nantinya menghasilkan jumlah karakter yang dicari
# Contoh penulisan (data.find("karakter yang ingin dicari"))


# CASE (Review Introducing String)
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())
print(highlighted_poems_stripped)

highlighted_poems_details = []
for poems in highlighted_poems_stripped:
    highlighted_poems_details.append(poems.split(":"))
print(highlighted_poems_details)
titles = []
poets = []
dates = []
for names in highlighted_poems_details:
    titles.append(names[0])
    poets.append(names[1])
    dates.append(names[2])

for final in range (0,len(highlighted_poems_details)):
    print(f"The poem {titles[final]} was published by {poets[final]} in {dates[final]}")
