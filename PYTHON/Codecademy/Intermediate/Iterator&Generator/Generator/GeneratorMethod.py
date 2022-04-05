# Pada generator terdapat method salah satunya adalah send.
# send() digunakan untuk mengirimkan nilai ke generator menggunakan ekspresi hasil
# Jika Anda menetapkan hasil ke variabel, argumen yang diteruskan ke metode .send() akan ditetapkan ke
# variabel itu. Memanggil .send() juga akan menyebabkan generator melakukan iterasi.
# Contoh:
def count_generator():
    while True:
        n = yield
        print(n)
my_generator = count_generator()
next(my_generator) # 1st Iteration Output: 
next(my_generator) # 2nd Iteration Output: None
my_generator.send(3) # 3rd Iteration Output: 3
next(my_generator) # 4th Iteration Output: None
my_generator.send(5) # 5th Iteration Output: 5
# contoh lainnya:
def generator():
    count = 0
    while True:
        n = yield count
        if n is not None:
            count = n
        count += 1
my_generator = generator()
print(next(my_generator)) # Output: 0
print(next(my_generator)) # Output: 1
print(my_generator.send(3)) # Output: 4
print(next(my_generator)) # Output: 5

# Contoh program sederhananya:
MAX_STUDENTS = 50 # constant karena pada python constant dituliskan huruf kapital 

def get_student_ids():
    student_id = 1
    while student_id <= MAX_STUDENTS:
        # Write your code below
        n = yield student_id
        if n is not None:
            student_id = n
            continue
        student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
    # Write your code below:
    if i == 1:
        i = student_id_generator.send(25)
    print(i)


# Method lainnya yang dimiliki pada generator yaitu throw dimana Anda dapat mengirimkan error ke generator
# throw() method ini keuntungannya digunakan jika kita perlu mengakhiri generator setelah mencapai nilai
# tertentu atau memenuhi kondisi tertentu.
# Penulisan throw() method: throw(errorkondisi, errormessage)
# Contoh:
def generator():
    i = 0
    while True:
        yield i
        i += 1
my_generator = generator()
for item in my_generator:
    if item == 3:
        my_generator.throw(ValueError, "Bad value given") # => ValueError: Bad value given jika item = 3

# Contoh lainnya:
def student_counter():
    for i in range(1,5001):
        yield i

student_generator = student_counter()
for student_id in student_generator:
    # Write your code below:
    if student_id > 100:
        student_generator.throw(ValueError, "Invalid student ID")


    print(student_id)

# Kemudian selain send() dan throw() method yang dapat kita gunakan pada generator adalah close() method.
# close() method digunakan untuk mengakhiri generator.
# Metode generator .close() digunakan untuk menghentikan generator lebih awal. Setelah metode .close()
# dipanggil, generator selesai seperti akhir dari perulangan for. Upaya iterasi lebih lanjut akan memunculkan
# pengecualian StopIteration.
# Contoh:
def generator():
    i = 0
    while True:
        yield i
        i += 1
my_generator = generator()
next(my_generator)
next(my_generator)
my_generator.close()
next(my_generator) # raises StopGenerator exception
# Contoh lainnya:
def generator():
    i = 0
    while True:
        try:
            yield i
        except GeneratorExit: # GeneratorExit exception
            print("Early exit, BYE!")
            break
    i += 1
my_generator = generator()
for item in my_generator:
    print(item)
    if item == 1:
        my_generator.close()# raises GeneratorExit exception and prints "Early exit, BYE!" 
                            # karena sudah diberi kondisi pada baris 102

# Contoh lainnya:
def student_counter():
    for i in range(1,5001):
        yield i

student_generator = student_counter()
for student_id in student_generator:
    print(student_id)
    # Write your code below:
    if student_id >= 100:
        student_generator.close()