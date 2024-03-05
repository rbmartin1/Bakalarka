import plistlib

def create_large_plist(file_path):
    # Create a large binary plist file with a large number of nested elements
    large_data = {"key{}".format(i): {"nested{}".format(j): {"data": "value"} for j in range(1000)} for i in range(1000)}
    
    # Write the large data to a binary plist file
    with open(file_path, "wb") as f:
        plistlib.dump(large_data, f, fmt=plistlib.FMT_BINARY)
    print("Large plist file created successfully!")

def create_good_plist(file_path):
    # Create a smaller binary plist file with a reasonable amount of data
    good_data = {"key1": {"nested1": {"data": "value"}}}
    
    # Write the good data to a binary plist file
    with open(file_path, "wb") as f:
        plistlib.dump(good_data, f, fmt=plistlib.FMT_BINARY)
    print("Good plist file created successfully!")

def load_plist_safely(file_path, max_size=10_000_000):
    # Attempt to read the plist file safely with a size limit
    try:
        with open(file_path, "rb") as f:
            data = f.read(max_size)
            plist_data = plistlib.loads(data)
        print("Data loaded successfully!")
        return plist_data
    except Exception as e:
        print("Error occurred while loading data:", e)
        return None

# Create a large binary plist file
create_large_plist("large_data.plist")

# Create a good binary plist file
create_good_plist("good_data.plist")

# Attempt to load the large plist file (vulnerable scenario)
loaded_large_data = load_plist_safely("large_data.plist")

# Attempt to load the good plist file (safe scenario)
loaded_good_data = load_plist_safely("good_data.plist")
