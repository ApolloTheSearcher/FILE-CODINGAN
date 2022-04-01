# Import modules above this line
# 2. Impor daftar siswa dari roster.py dan impor modul itertools
import itertools
import roster

class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sort_alphabetically(roster.student_roster)
# 3a. Tentukan protokol iterator untuk kelas ClassroomOrganizer kami dengan menggunakan metode __iter__ dan __next__
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        eachStudent = self.sorted_names[self.index]
        self.index += 1
        if self.index >= 10:
            raise StopIteration
        return eachStudent
    
    def _sort_alphabetically(self,students):
        names = []
        for student_info in students:
            name = student_info['name']
            names.append(name)
        return sorted(names)

    def get_students_with_subject(self, subject):
        selected_students = []
        for student in roster.student_roster:
            if student['favorite_subject'] == subject:
                selected_students.append((student['name'], subject))
        return selected_students
# 4. Buat method table_seating untuk siswa menggunakan modul itertools(itertools yang di pakai itu combinations)
# di dalam kelas ClassroomOrganizer
    def table_seating(self):
        names_set = []
        for student_setting in roster.student_roster:
            name = student_setting['name']
            names_set.append(name)
            # final list of all tuple combinations of 2 students that can be seated at each table
            table_list = list(itertools.combinations(names_set, 2)) # itertools)
        return table_list
# 5. Metho untuk ambil daftar semua 4 kombinasi siswa yang mata pelajaran favoritnya adalah Matematika dan Sains
    def two_subject_students(self):
        math = []
        science = []
        for student_subject in roster.student_roster:
            fav_subject = student_subject['favorite_subject']
            if fav_subject == 'Math':
                math.append(student_subject['name'])
            if fav_subject == 'Science':
                science.append(student_subject['name'])
            two_list_chain = itertools.chain(math, science)
            two_list_combinations = list(itertools.combinations(two_list_chain, 4))
        return two_list_combinations
# Setelah jadi fungsi ke 5 ini kita bisa menggunakan methodnya di folder script.py

    
# 3b. Buat cara untuk menjalankan panggilan masuk pagi, dengan memesan semua siswa dengan nama depan menurut abjad
student_roll = ClassroomOrganizer()
student_roll_iter = iter(student_roll) 
for student in student_roll_iter: # Loopingnya untuk berurutan
    print(student)

# Memanggil table setting dan di pindahkan kedalam variable 
tables = ClassroomOrganizer()
student_tables = tables.table_seating()  # digunakan untuk memanggil method table_seating di script.py
print(student_tables)

# memanggil method untuk mendapatkan daftar semua 4 kombinasi siswa yang mata pelajaran favoritnya adalah Matematika dan Sains
subject = ClassroomOrganizer()
student_subject = subject.two_subject_students() # digunakan untuk memanggil method two_subject_students di script.py
print(student_subject)
