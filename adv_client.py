import socket
from PIL import Image

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((socket.gethostname(),4571))

    # custom_file = open('files\received_file.txt','wb')
    with open('files/received_image.jpg','wb') as image_file:


        while True:

            data = s.recv(40960)

            if not data:
                print("No messages from server")
                break

            image_file.write(data)
            print('Data sent')