# Pada unit testing, kita menggunakan keyword "try" dan "except"
# dimana prosesnya hampir sama seperti if else statement.
# tetapi biasanya digunakan untuk perulangan karena mengecek satu satu guys.
'''
Pembahasan lebih jelasnya:
Sejauh ini, expection yang kami temui telah menyebabkan program kami berhenti dijalankan.
Namun, ada kemungkinan bagi program untuk terus mengeksekusi bahkan setelah menemukan pengecualian.
Proses ini dikenal sebagai expection handling dan dilakukan dengan menggunakan klausa try/except Python.
Contoh penggunaan:
'''
staff = {
    'Austin': {
        'floor managers': 1,
        'sales associates': 5
    },
    'Melbourne': {
        'floor managers': 0,
        'sales associates': 8
    },
    'Beijing': {
        'floor managers': 2,
        'sales associates': 5
    },
}

def print_staff_report(location, staff_dict):
    managers = staff_dict['floor managers']
    sales_people = staff_dict['sales associates']
    ratio = sales_people / managers
    print('Instrument World ' + location + ' has:')
    print(str(sales_people) + ' sales employees')
    print(str(managers) + ' floor managers')
    print('The ratio of sales people to managers is ' + str(ratio))
    print()

for location, staff in staff.items():
    # Write your code below:
    # Contoh try dan except:
    try:
        print_staff_report(location, staff)
    # except:
    #     print("Could not print sales report for " +location)
    except ZeroDivisionError as err: # => kalau misalnya kita catching spesifik sih exception yang kita inginkan
        print("Could not find staff for " + location)
        print(err)
        
# Selain itu pada except juga bisa kita lebih spesifikasikan bila error nya berasal dari mana.
# Terus kita juga bisa multiple except untuk menangani beberapa error.
# Contoh:
instrument_prices = {
    'Cello': 1000,
    'Banjo': 200,
    'Flute': 100,
}

def display_discounted_price(instrument, discount):
    full_price = instrument_prices[instrument]
    discount_percentage = discount / 100
    discounted_price = full_price - (full_price * discount_percentage)
    print("The instrument's discounted price is: " + str(discounted_price))

instrument = 'Banjo'
discount = '20'

# Write your code below:
try:
    display_discounted_price(instrument, discount)
except KeyError:
    print("An invalid instrument was entered!")
except TypeError:
    print("Discount percentage must be a number!")
except Exception:
    print("Hit an exception other than KeyError or TypeError!")

