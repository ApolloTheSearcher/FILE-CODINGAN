# Pada generator kita bisa menggabungkan semua fungsi menjadi satu atau menggabungkan semua yield yang 
# terdapat pada fungsi fungsi menjadi satu fungsi atau juga fungsinya sama dengan method chain() pada itertools
'''
Ada beberapa kasus di mana berguna untuk menghubungkan beberapa generator menjadi satu.
Ini memungkinkan kita untuk mendelegasikan operasi satu generator ke sub-generator lain.
Generator Connection mirip dengan menggunakan fungsi itertools chain() untuk menggabungkan iterator
menjadi satu iterator.
'''
# Contoh program:
def cs_courses():
    yield 'Computer Science'
    yield 'Artificial Intelligence'
def art_courses():
    yield 'Intro to Art'
    yield 'Selecting Mediums'
def all_courses():
    yield from cs_courses() # menggabungkan generator cs_courses()
    yield from art_courses() # menggabungkan generator art_courses()
combined_generator = all_courses()

# Contoh lainnya:
def science_students(x):
    for i in range(1,x+1):
        yield i

def non_science_students(x,y):
    for i in range(x,y+1):
        yield i
        

# Write your code below
def combined_students():
    yield from science_students(5) # menggabungkan generator science_students(x) x bernilai 5
    yield from non_science_students(10,15) # 10,15 adalah parameter dari fungsi non_science_students()
    yield from non_science_students(25,30)

student_generator = combined_students()
for student in student_generator:
    print(student)


# Kemudian selain cara menggabungkan generator menjadi satu dengan cara diatas kita juga dapat menggunakan
# cara yaitu dengan menggunakan Generator Pipelines dimana kita menggabungkan fungsi generator yang None parameternya
# fungsi itu kita masukan ke dalam fungsi generator yang memiliki parameter sehingga parameter yang diisi yaitu berisi fungsi
# yang parameternya None.
# Contoh:
def number_generator():
    i = 0
    while True:
        yield i
        i += 1

def even_number_generator(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

even_numbers = even_number_generator(number_generator()) # Generator Pipelines terjadi disini 

for e in even_numbers:
    print(e)
    if e == 100:
        break

# Contoh lainnya:
def course_generator():
    yield ("Computer Science", 5)
    # Write your code below:
    yield ("Art", 10)
    yield ("Business", 15)
def add_five_students(courses):
    for courses, num_student in courses:
        yield (courses, num_student + 5)
increased_courses = add_five_students(course_generator()) # Generator Pipelines terjadi disini
for student_all in increased_courses:
    print(student_all)

