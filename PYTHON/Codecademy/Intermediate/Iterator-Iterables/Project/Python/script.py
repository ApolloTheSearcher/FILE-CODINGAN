# New teacher in town (PROJECT FOR Iterator-Iterables)
import roster
import class_organizer

class Student:
    def __init__(self, student_list):
        self.studentList = student_list
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index < len(roster.student_roster):
            student_status = self.studentList[self.index]
            self.index += 1
            return student_status
        else:
            raise StopIteration
        
# 1. Buat iterator untuk daftar student_roster dan cetak informasi setiap siswa menggunakan next()
student_list = Student(roster.student_roster)
student_list_iter = iter(student_list)
print(next(student_list_iter))
print(next(student_list_iter))
print(next(student_list_iter))
print(next(student_list_iter))
print(next(student_list_iter))
print(next(student_list_iter))
print(next(student_list_iter))

# 4. print the final dari method table_seating
print(class_organizer.student_tables)

# 5. print the final dari two_subject_students yang mengambil semua 4 kombinasi siswa yang pelajaran favoritnya adalah Matematika dan Sains
print(class_organizer.student_subject)

