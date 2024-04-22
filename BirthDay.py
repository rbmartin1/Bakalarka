import hashlib
import os
import binascii

def secure_hash(x, salt=None):
    """
    Zabezpečená hash funkcia: Hashuje vstup pomocou SHA-256 s voliteľnou salt.
    Ak nie je zadaná žiadna salt, vygeneruje novú salt.
    Vráti hash a použitú salt.
    """
    if salt is None:
        # Generovanie 16byte salt
        salt = os.urandom(16)
    # pou6itie salt, kalkulacia hashu
    hash_value = hashlib.sha256(salt + x.encode()).hexdigest()
    return hash_value, binascii.hexlify(salt).decode()

def find_secure_collision(num_samples):
    """
    Pokus o nájdenie kolízie v bezpečnom nastavení hashovania.
    Je to podstatne ťažšie vďaka salt a použitiu SHA-256.
    """
    hashes = {}
    for _ in range(num_samples):
        # Nahodny retazec
        random_string = str(os.urandom(8))
        # Vyratanie hashu 
        hash_value, salt = secure_hash(random_string)
        if hash_value in hashes:
            print(f"Collision found: {random_string} (salt: {salt}) and {hashes[hash_value][0]} (salt: {hashes[hash_value][1]}) both hash to {hash_value}")
            return random_string, hashes[hash_value][0], hash_value
        hashes[hash_value] = (random_string, salt)
    return None

# Volanie funkcie
result = find_secure_collision(10000)  
if result:
    print(f"Collision details: {result}")
else:
    print("No collision was found within the sample size.")

