# Kita disini dapat membaca sebuah file Json dengan menggunakan pythonnya
'''
cara nya hampir sama dengan sebelum-sebelumnya, dengan menggunakan with open:
import json => jangan lupa import jsonnya
with open('nama file Jsonnya') as variable_bebas
    message = json.load(variable_bebas)
    print(message['text'])
'''

'''
kita juga dapat writing sebuah file json dengan menggunakan python
contoh penulisan dan casenya:
data_payload = [
    {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
    'follow up': 'But enough talk!'}
]
import json
with open('data.json', 'w') as data_json: => 'w' disini artinya untuk write ya ada istilah lainnya
    json.dump(data_payload, data_json)

'''