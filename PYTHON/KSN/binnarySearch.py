def mencariSquentialSearch (data, key):
    print(f"Data yang dicari adalah {key} pada kumpulan datanya {data}")
    wadah = []
    for i in range(len(data)):
        if data[i] == key:
            wadah.append(i)
    if len(wadah) >= 0:
        print(f"data {key} ditemukan pada index {wadah}")
    else:
        print("data tidak ditemukan")

def mencariBinarySearch(data, key):
    pos = []
    for i in range (len(data)):
        status = False
        
    
data = [10, 14 ,19, 27, 31, 33, 35, 42, 44, 35]
key = 35
mencariSquentialSearch(data, key)