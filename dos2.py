import plistlib

def create_large_plist(file_path):
    # Vytvorenie veľkého binárneho súboru plist s veľkým počtom vnorených prvkov
    large_data = {"key{}".format(i): {"nested{}".format(j): {"data": "value"} for j in range(1000)} for i in range(1000)}
    
    # Zápis údajov do binárneho súboru
    with open(file_path, "wb") as f:
        plistlib.dump(large_data, f, fmt=plistlib.FMT_BINARY)
    print("Large plist file created successfully!")

def create_safe_plist(file_path):
    # Vytvorenie menšieho binárneho súboru plist s primeraným množstvom údajov
    safe_data = {"key1": {"nested1": {"data": "value"}}}
    
    # Zápis údajov do binárneho súboru
    with open(file_path, "wb") as f:
        plistlib.dump(safe_data, f, fmt=plistlib.FMT_BINARY)
    print("Safe plist file created successfully!")

def load_plist_safely(file_path, max_size=10_000_000):
    # Pokus o bezpečné čítanie súboru plist s obmedzením veľkosti
    try:
        with open(file_path, "rb") as f:
            data = f.read(max_size)
            plist_data = plistlib.loads(data)
        print("Data loaded successfully!")
        return plist_data
    except Exception as e:
        print("Error occurred while loading data:", e)
        return None

# Vytvorenie veľkého binárneho súboru plist
create_large_plist("large_data.plist")

# Vytvorenie bezpečného binárneho súboru plist
create_safe_plist("safe_data.plist")

# Pokus o načítanie veľkého súboru plist - zraniteľný scenár
loaded_large_data = load_plist_safely("large_data.plist")

# Pokus o načítanie bezpečného súboru plist - bezpečný scenár
loaded_safe_data = load_plist_safely("safe_data.plist")
