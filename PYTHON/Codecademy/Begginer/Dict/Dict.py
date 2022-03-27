'''
Penulisan dict itu {key:value} itu saja sih kalau dict itu ada key dan value
dan kita juga menambah sebuah key nya
cara penulisannya nya
dict[key] = value
yaitu dengan cara, contoh:
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
jika kita ingin menambahkan key nya dan value
menu["chocolate cake"] = 4
'''
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["chocolate cake"] = 4
# kan kalau di atas itu bila kita menambahkan key nya dan value satu persatu kita dapat menambahkan langsung sekaligus
# dengan menggunakan .update()
# caranya => variable.update({key:value})
menu.update({"chocolate cake": 4, "chocolate chip cookie": 12, "juice": 10})
# kita juga mengganti value nya
# cara mengganti value nya => variable[key] = valueyangbaru

