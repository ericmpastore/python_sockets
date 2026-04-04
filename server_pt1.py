import socket
import pickle
import time
from product import Product

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(),4571))

    # python_dictionary = {'a':1,'b':2}
    # pickled_dictionary = pickle.dumps(python_dictionary)
    # custom_object = Product('P024','Torch',13)
    # pickled_object = pickle.dumps(custom_object)

    custom_objects = [Product('P024','Torch',13),
                      Product('P025','WaterBottle', 5),
                      Product('P026','Keyboard', 20),
                      Product('P027','Mouse', 15),
                      Product('P028','USBCable', 2)]

    s.listen(5)

    print('Server is up and listening.')

    # Open client connection, EPastore 04/04/2026
    client, address = s.accept()
    print(f"Connection to {address} has been established.\n")
    print(f"Client object is {client} \n")

    # Send both python objects over socket connection, EPastore 04/04/2026
    # client.send(pickled_dictionary)
    # client.send(pickled_object)

    for product in custom_objects:
        pickled_product = pickle.dumps(product)
        client.send(pickled_product)

        print(f"Sent product: {product.pid}")

        time.sleep(2)
