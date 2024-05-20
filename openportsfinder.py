import socket
import concurrent.futures
import threading

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return port

def scan_ports(ip, start_port, end_port):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers = max_worker) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in concurrent.futures.as_completed(futures):
            port = future.result()
            if port:
                open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    target_ip = str(input("Enter the IP address to scan = "))
    start_port = int(input(f"Enter the starting port number to scan for {target_ip} = "))
    end_port = int(input(f"Enter the ending port number to scan for {target_ip} = "))
    max_worker = int(input("Enter the maximum number of workers to use = "))

    print(f"Scanning open ports on {target_ip} from {start_port} to {end_port}...")
    open_ports = scan_ports(target_ip, start_port, end_port)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")
