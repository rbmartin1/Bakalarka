import hashlib
import random

# zranitelna fukncia - chyba overenie ci dany hash uz neexistuje
def hash_function(data):
    return hashlib.sha256(data.encode()).hexdigest()

def generate_collision():
    hash_table = {}
    print("hello")

    while True:
        # Vytvorenie inputu
        data = str(random.getrandbits(128))

        # Hash inputu
        hash_value = hash_function(data)

        # Kontrola ci dany hash sme uz vytvorili
        if hash_value in hash_table:
            # Najdenie kolizie a vratenie vstupnych dat s rovnakym hashom
            return data, hash_table[hash_value]
        else:
            # pridanie - pokracovanie 
            hash_table[hash_value] = data

# Vykonanie utoku
input1, input2 = generate_collision()


print("Input 1:", input1)
print("Input 2:", input2)
print("Hash of Input 1:", hash_function(input1))
print("Hash of Input 2:", hash_function(input2))
