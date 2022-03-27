'''
Pada tingkat akses tertinggi, kami memiliki cakupan global. Nama yang ditentukan dalam namespace global akan
secara otomatis dicakup secara global dan dapat diakses di mana saja dalam program kami.
'''
# Contoh kasus dengan menggunakan Global Scope
def print_available(color):
    paint_gallons_available = {
        'red': 50,
        'blue': 72,
        'green': 99,
        'yellow': 33
}
    print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


def print_all_colors_available():
    for color in paint_gallons_available:
        print(color)

print_available('red')
print_all_colors_available()
# Ketika kita keluarkan outputnya akan error nah pada kasus ini kita harus menggunakan global scope
# Menjadi:
paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
}
def print_available(color):

    print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


def print_all_colors_available():
    for color in paint_gallons_available:
        print(color)
print_available('red')
print_all_colors_available()

'''
Selain itu kita juga dapat memodifikasi tanpa memindah kan tempat yang ingin di jadikan global
Contoh kasus di atas, jika kita menggunakan global akan menjadi seperti ini:
'''
def print_available(color):
    global paint_gallons_available
    paint_gallons_available = {
        'red': 50,
        'blue': 72,
        'green': 99,
        'yellow': 33
}
    print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


def print_all_colors_available():
    for color in paint_gallons_available:
        print(color)

print_available('red')
print_all_colors_available()
