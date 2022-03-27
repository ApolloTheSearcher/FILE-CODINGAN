"""
sama seperti reading files untuk membuka csv
dengan cara:
with open ('nama file csv') as variablebebascsv:
    print(variablebebascsv.read()) => digunakan untuk menghasilkan si file csvnya
"""
'''
cara reading files csv
import csv
with open('namafilecsvnya') as variablebebascsv:
    variablebebas = csv.DictReader(variablebebascsv)
jika ingin menggunakan for loop
    for variable in variablebebas:
        print(variable[isinya apa saja])
'''

"""
selain itu kita juga dapat dapat writing file csv dengan cara:
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'},
{'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'},
{'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'},
{'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'},
{'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'},
{'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'},
{'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'},
{'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'},
{'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'},
{'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
with open('logger.csv', 'w') as logger_csv:
    log_writer = csv.DictWriter(logger_csv, fields)
    log_writer.writeheader()
    for item in access_log:
        log_writer.writerow(item)
"""

