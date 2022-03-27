# Contoh program Enclosing_Local Scope:
def calc_paint_amount(width, height):
    square_feet = width * height

# Write your code below!
    def calc_gallons():
        return square_feet / 400


    return calc_gallons()
    

print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30,20)))

# Moditifikasi suatu program Nonlocal Scope:
walls = [(20, 9), (25, 9), (20, 9), (25, 9)]


def calc_paint_amount(wall_measurements):

    square_feet = 0

    def calc_square_feet():
    
        for width, height in wall_measurements:
            nonlocal square_feet # menggunakan nonlocal untuk mengakses variabel global dalam fungsi ini
            # Kalau kita gk pake nonlocal dia akan error
            square_feet += width * height

    def calc_gallons():
        return square_feet / 400

    calc_square_feet()

    return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(walls)))

