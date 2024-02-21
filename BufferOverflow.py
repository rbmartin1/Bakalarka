import ctypes

# Buffer size
BUFFER_SIZE = 10

# Allocate buffer
buffer = ctypes.create_string_buffer(b"\x00" * BUFFER_SIZE)

def main():

    # Attacker's input longer than the buffer
    user_input = "A" * (BUFFER_SIZE - 1)  # Adjusted to fit within buffer size

    # Perform buffer overflow by directly writing to memory
    buffer.raw = user_input.encode()

    # Check the buffer after the overflow
    print("Buffer after overflow:", buffer.raw)

if __name__ == "__main__":
    main()
