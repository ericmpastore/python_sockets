import socket 

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:

    server_name = input('Enter your name: ')

    sock.bind((socket.gethostname(),4571))

    sock.listen(5)
    print(f"{server_name} is up and listening...")

    client, address = sock.accept()
    print(f'Connection to {address} established.\n')
    print(f'Client object: {client}\n')

    client_name_raw = client.recv(1024)
    client_name = client_name_raw.decode()
    print(f'Client {client_name} has initiated a connection.')

    client.send(server_name.encode()) #default is utf-8

    while True:

        send_message = input(server_name + ' - ')
        client.send(send_message.encode())

        if send_message.lower() == "bye":
            break

        message_recv = client.recv(1024)
        message_recv = message_recv.decode()
        print(client_name, ' - ', message_recv)



