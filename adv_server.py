import socket
from PIL import Image

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((socket.gethostname(),4571))
    s.listen(5)
    print("Server is up, listening...\n")

    client, address = s.accept()
    print(f"Connection to {address} has been established.\n")
    print(f"Connection established: {client}\n")

    # Removed to switch to image file, EPastore 04/07/2026
    # custom_file = open('files\pg2680.txt','rb')

    # custom_data = custom_file.read(40960)

    # while(custom_data):
    #     client.send(custom_data)
    #     custom_data = custom_file.read(40960)
                                       
    # print("Custom file sent")

    with open('files/cute_dog.jpg','rb') as image_file:

        image_batch = image_file.read(40960)

        while(image_batch):
            client.send(image_batch)
            image_batch = image_file.read(40960)
            print("Data sent to server.")

print("Image sent successfully.")