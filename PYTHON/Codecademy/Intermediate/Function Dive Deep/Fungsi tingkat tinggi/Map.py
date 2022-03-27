# Built in Higher Order Functions
'''
Pada bahasa python mempunyai fungsi tingkat tinggi bawaan python, Berikut bagian dari 3 fungsi tingkat tinggi
yang berbeda:
1. map()
2. filter()
3. reduce()
Bersama-sama, ketiga fungsi ini adalah beberapa fungsi tingkat tinggi yang paling banyak digunakan dan kuat
di Python dan akan membantu kita meningkatkan program Python
'''
# Map()
# Penulisannya => returned_map_object = map(function, iterable)
# Function pada parameter map itu digunakan dari namafungsi yang kita buat
# Iterable pada parameter adalah nama array yang kita buat
# Contoh Map() dibawah tidak pakai lambda:

grade_list = [3.5, 3.7, 2.6, 95, 87]

# Your code below:
def grade(x):
    if x <= 4.0:
        return x * 25
    else:
        return x
# assign the result of your map function to the variable grades_100scale

grades_100scale = map(grade, grade_list)

# convert grades_100scale to a list and save it as updated_grade_list 
updated_grade_list = list(grades_100scale)
# print updated_grade_list
print(updated_grade_list)

# ========================================================================

# Contoh Map() dibawah pakai lambda:
grade_list = [3.5, 3.7, 2.6, 95, 87]

# Your code below:
# assign the result of your map function to the variable grades_100scale
grades_100scale = map(lambda grade: grade * 25 if grade <= 4.0 else grade, grade_list)
# grade disitu pada lambda adalah parameter ya bukan nama fungsi
# convert grades_100scale to a list and save it as updated_grade_list 
updated_grade_list = list(grades_100scale)
# print updated_grade_list
print(updated_grade_list)


