import sqlite3

# Vytvorenie SQLlite databazy
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Vytvorenie tabulky s nazvom users s atributami id, username a password
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    
    # Naplnenie databazy s datami admin, user1 a user2
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'adminpassword'))
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('user1', 'user1password'))
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('user2', 'user2password'))
    
    # Commit zmien a ukončenie prepojenia
    conn.commit()
    conn.close()

# Funkcia login so zranitelnym inputom a query
def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Zranitelna SQL query - priame použitie vstupu
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    
    cursor.execute(query)
    result = cursor.fetchone()
    
    conn.close()
    return result

# kontrola uspesnoti prihlasenia
def log(result):
    if result:
        print("Login successful!")
    else:
        print("Invalid username or password.")


create_database()

# Použivatelsky vstup - spravne heslo, bez pokusu o utok
username1 = "admin"
password1 = "adminpassword" 

# Použivatelsky vstup - nebezpečny skrz username '--
username2 = "admin'--"
password2 = "1234" 

# Použivatelsky vstup - zle heslo, bez pokusu o utok
username3 = "admin"
password3 = "1234" 



result = login(username1, password1)
log(result)

# Pokus o SQL injection
result = login(username2, password2)
log(result)

result = login(username3, password3)
log(result)




