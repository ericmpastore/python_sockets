import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

    s.connect((socket.gethostname(),4571))

    while True:

        msg = s.recv(1024)

        if not msg:
            print("No messages from the server. Closing connection.")
            break
            s.close()

        # print(f"Type of received message: {type(msg)}")
        # print(f"Message from server: {msg}")

        product_object = pickle.loads(msg)

        # print(f"Type of deserialized message: {type(unpickled_msg)}")
        # print(f"Deserialized data: {unpickled_msg}")
        print(f"Product ID: {product_object.pid}\nProduct Name: {product_object.pname}\nProduct Price: {product_object.pprice}\n\n")