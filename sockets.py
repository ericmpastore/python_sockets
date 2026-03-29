# first demo for sockets package
# EPastore, 03/29/2026

import socket

def main():
    host_name = socket.gethostname()
    print(host_name)
    host_addr = socket.gethostbyname(socket.gethostname())
    print(host_addr)
    host_info = socket.gethostbyaddr('127.0.0.1')
    print(host_info)
    

if __name__ == "__main__":
    main()