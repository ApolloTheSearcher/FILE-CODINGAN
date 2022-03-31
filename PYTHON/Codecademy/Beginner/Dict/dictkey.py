# # kita juga ternyata dapat memanggil semua key atau value pada dict
# # dengan cara menggunakan for each
# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# # Dibawah ini menggunakan cara biasa
# users = user_ids.keys()
# lessons = num_exercises.keys()
# print(users)
# print(lessons)
# # Dibawah ini menggunakan for each
# for user in user_ids.keys():
#     print(user)
#     for num in num_exercises.keys():
#         print(num)

# # Selain itu kita juga bisa mencari value nya juga dengan cara
# # for each atau biasa:
# # Contoh mencari value nya
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# total_exercises = 0
# for exercises in num_exercises.values():
#     total_exercises += exercises
# print(total_exercises)


# # Selain itu kita juga dapat mencari/memanggil keduany key dan value nya
# pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

# for keys, values in pct_women_in_occupation.items():
#     print(f"Women make up {values} percent of {keys}s.")  

