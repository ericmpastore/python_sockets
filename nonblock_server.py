from datetime import datetime
import socket 

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:

    sock.bind((socket.gethostname(),4571))

    sock.listen(5)
    print("Server is up and listening...")

    client, address = sock.accept()
    print(f'Connection to {address} established.\n')
    print(f'Client object: {client}\n')

    start_time = datetime.now()

    data = client.recv(1024)
    total_received = len(data)

    i = 1

    while data:
        print(data.decode('utf-8'))
        data = client.recv(1024)

        total_received += len(data)
        i+=1

    print(f"All data received in {i} batches.")
    client.close()

end_time = datetime.now()
print(f"Duration: {end_time-start_time}")
print(f"Size of data received: {total_received}")