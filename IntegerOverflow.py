import array
import sys

def safe_integer_operation():
    # list i
    arr = array.array('i', [0])

    # Max hodnota pre 32-bit signed integer
    max_int32 = 2147483647
    min_int32 = -2147483648

    arr[0] = max_int32
    try:
        # Kontrola pred inkrementáciou, aby sa zabránilo pretečeniu
        if arr[0] < max_int32:
            arr[0] += 1
        else:
            raise OverflowError("Attempted to increment beyond the maximum limit for a 32-bit signed integer.")
        
        print(f"Value after safe increment: {arr[0]}")
    except OverflowError as e:
        print(f"OverflowError: {e}")

def main():
    safe_integer_operation()

if __name__ == "__main__":
    main()
