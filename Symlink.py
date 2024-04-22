<<<<<<< HEAD
import os

def vulnerable_temp_file(data):
    # predpovedatelne dočasny priecinok
    temp_file_name = "/tmp/myapp_temp.txt"
    
    # zapis do priecinka
    with open(temp_file_name, 'w') as f:
        f.write(data)
    
    print(f"Processed temporary file: {temp_file_name}")


user_data = "Sensitive information"
vulnerable_temp_file(user_data)

# útočníkova časť
#ln -s /etc/passwd /tmp/myapp_temp.txt
=======
import os

def vulnerable_temp_file(data):
    # predpovedatelne dočasny priecinok
    temp_file_name = "/tmp/myapp_temp.txt"
    
    # zapis do priecinka
    with open(temp_file_name, 'w') as f:
        f.write(data)
    
    print(f"Processed temporary file: {temp_file_name}")


user_data = "Sensitive information"
vulnerable_temp_file(user_data)

# útočníkova časť
#ln -s /etc/passwd /tmp/myapp_temp.txt
>>>>>>> 41f6ab91d4f04711de12669a953e6b4873d38682
