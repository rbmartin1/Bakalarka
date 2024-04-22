import os
import stat

def is_symlink(filename):
    try:
        # Kontrola, či má súbor atribút reparse point, vyuzivany pre symlinky
        return os.stat(filename, follow_symlinks=False).st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT != 0
    except AttributeError:
        # Náhradný variant, ak nie sú podporované špecifické kontroly atribútov 
        return os.path.islink(filename)

def write_to_file_securely(filename, data):
    # overenie ci je symlink pomocou funckie
    if is_symlink(filename):
        raise ValueError("Cannot write to a symlink!")
    
    with open(filename, 'w') as f:
        f.write(data)

# Testy
try:
    file = 'realfile.txt'
    user_data = "Hello World..."
    write_to_file_securely(file, user_data)
    print("File written successfully.")
except ValueError as e:
    print(e)

symlink_file = 'symlinkfile'
try:
    write_to_file_securely(symlink_file, "This should not be written.")
    print("Symlink test failed: no error raised when writing to symlink.")
except ValueError as e:
    print("Symlink test passed: correctly raised an error.")

#File written successfully.
#Symlink test passed: correctly raised an error.
