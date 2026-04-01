import socket
#Script to listen for connections and return string to client.
#EPastore, 04/01/2026

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

    s.bind((socket.gethostname(),4571))

    s.settimeout(10)
    
    try:
        s.listen(5)

        print("Server is up. Listening for connections.")

        client, address = s.accept()
        print(f"Connection to {address} established.\n")
        print(f"Client connection: {client} \n")
        client.send(bytes("Hello! Welcome to socket programming.","utf-8"))

    except socket.timeout:
        print("The timeout has been exceeded. Please re-connect.")