'''
Nah kemudin ada yang namanya itu local namespace. kalau local namespace jika kita panggil di awal tanpa
adanya kegiatan seperti memasukan data kevariable, jika tidak pada localspace akan seperti keadaan awal/pabrik
jadi kalau local namespace eksekusinya saat memang memang yang ada di code program kita.
memanggilnya menggunakan locals()
Contoh program yang menggunakan local namespace :
'''
global_variable = 'global'

def add(num1, num2):
    nested_value = 'Inside Function'   
    print(num1 + num2)
    print(locals())
    
add(5, 10)
'''
Outputnya :
15
{'num1': 5, 'num2': 10, 'nested_value': 'Inside Function'}
'''
# Contoh program yang menggunakan local namespace :
global_variable = 'global'



print(' -- Local and global Namespaces with empty script -- \n')
# Write Checkpoint 1 here:
print(locals())
#print(globals())


# Write Checkpoint 2 here:
def divide(num1, num2):
    result = num1 / num2
    print(locals())


# Write Checkpoint 3 here:
def multiply(num1, num2):
    product = num1 * num2
    print(locals)




print(' \n -- Local Namespace for divide -- \n')
# Write Checkpoint 4 here:
divide(3, 4)


print(' \n -- Local Namespace for multiply -- \n')
# Write Checkpoint 5 here:
multiply(4, 50)


print(' \n -- Local Namespace final -- \n')
# Write Checkpoint 6 here:
print(locals())