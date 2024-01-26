import socket
import json

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("dm:d1:5k:df:46:62", 4)) # REPLACE with your actual Bluetooth device's MAC address

try:

    received_data = client.recv(1024)
    received_json = json.loads(received_data.decode('utf-8'))
    print("Received JSON data from server:", received_json)


    with open('client_received_dummy.json', 'w') as file:
        json.dump(received_json, file)


    with open('client_dummy.json', 'r') as file:
        dummy_data = json.load(file)


    data_to_send = json.dumps(dummy_data)
    client.send(data_to_send.encode('utf-8'))

except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
except socket.error as e:
    print(f"Socket error: {e}")

client.close()