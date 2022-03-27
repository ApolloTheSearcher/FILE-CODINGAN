# pada sebuah program python kita dapat menggunakan Try-Except untuk menghandle error fungsinya sama dengan
# if else loh
# contoh programmnya
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level["matcha"] = 30
try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Unknown Caffeine Level")
