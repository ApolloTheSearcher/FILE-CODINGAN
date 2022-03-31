# Import modules above this line
# 2. Import list of students from roster.py and import itertools module
import itertools
import roster

class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sort_alphabetically(roster.student_roster)
# 3a. Define the iterator protocol for our ClassroomOrganizer class
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
# 4. Create method table for student using itertools module within ClassroomOrganizer class
    def table_seating(self):
        names_set = []
        for student_setting in roster.student_roster:
            name = student_setting['name']
            names_set.append(name)
            # final list of all tuple combinations of 2 students that can be seated at each table
            table_list = list(itertools.combinations(names_set, 2))
        return table_list

    
# 3b. Create a way to run though morning roll call, by ordering all student by first name alphabetically
student_roll = ClassroomOrganizer()
student_roll_iter = iter(student_roll)
for student in student_roll_iter:
    print(student)

# Memanggil table setting dan di pindahkan kedalam variable 
tables = ClassroomOrganizer()
student_tables = tables.table_seating()
print(student_tables)
