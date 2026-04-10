import socket
from PIL import Image

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((socket.gethostname(),4571))

    s.setblocking(True)

    data = bytes('Hello Server\n','utf-8') *1024*1024*10
    print(f"Size of data sent: {len(data)}")

    assert s.send(data)

    # custom_file = open('files\received_file.txt','wb')
    # with open('files/received_image.jpg','wb') as image_file:


    #     while True:

    #         data = s.recv(40960)

    #         if not data:
    #             print("No messages from server")
    #             break

    #         image_file.write(data)
    #         print('Data sent')