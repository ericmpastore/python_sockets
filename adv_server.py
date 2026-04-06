import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((socket.gethostname(),4571))
    s.listen(5)
    print("Server is up, listening...\n")

    client, address = s.accept()
    print(f"Connection to {address} has been established.\n")
    print(f"Connection established: {client}\n")

    custom_file = open('files\pg2680.txt','rb')

    custom_data = custom_file.read(40960)

    while(custom_data):
        client.send(custom_data)
        custom_data = custom_file.read(40960)
                                       
    print("Custom file sent")