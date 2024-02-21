import ctypes

# Buffer - makro pre velkost
BUFFER_SIZE = 10

# Alokacia
buffer = ctypes.create_string_buffer(b"\x00" * BUFFER_SIZE)

def main():

    # Utocnikov vstup vacsi ako buffer
    user_input = "A" * (BUFFER_SIZE + 2)

    # Vykonanie utoku priamym zapisanim do pamate
    ctypes.memmove(buffer, user_input.encode(), len(user_input))

    # Vypis po utoku
    print("Buffer after overflow:", buffer.raw)

if __name__ == "__main__":
    main()
