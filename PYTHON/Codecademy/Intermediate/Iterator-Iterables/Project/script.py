# New teacher in town (PROJECT FOR Iterator-Iterables)
import roster
import itertools
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
        
# 1. Create iterator for student_roster list and print out each student's information using next()
student_list = Student(roster.student_roster)
student_list_iter = iter(student_list)
print(next(student_list_iter))
print(next(student_list_iter))
print(next(student_list_iter))
print(next(student_list_iter))
print(next(student_list_iter))
print(next(student_list_iter))
print(next(student_list_iter))

# 4. print out the result to see all the possible table combinations of two student 
print(class_organizer.student_tables)

# 5