# Simulacia databazy
user_database = {
    "admin": "password123",
    "user1": "123456",
    "user2": "password456",
    "root": "pass"
}


def login(username, password):

    if username in user_database and user_database[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Pokus o prihlasenie so spravnymi udajmi
login("admin", "password123")
# Pokus o prihlasenie s nespravnymi udajmi
login("Janko", "heslo")

# Bypass prihlasenia priamym pristupom do databazy
print("Attempting to bypass the login:")
print("Welcome, root!" if "root" in user_database else "Access denied")
print("Welcome, admin!" if "admin" in user_database else "Access denied")
