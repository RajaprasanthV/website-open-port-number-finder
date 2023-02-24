import socket

def scan_host(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open on {host}.")
        sock.close()
    except:
        print(f"Unable to scan host {host}.")

def main():
    host = input("Enter the host to scan: ")
    for port in range(1, 65535):
        scan_host(host, port)

if __name__ == '__main__':
    main()
