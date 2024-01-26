import socket
import json

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    server.bind(("dm:d1:5k:df:46:62", 4))   # REPLACE with your actual Bluetooth device's MAC address
    server.listen(1)

    client, addr = server.accept()

    try:
        with open('server_dummy.json', 'r') as file:
            dummy_data = json.load(file)

        data_to_send = json.dumps(dummy_data)
        client.send(data_to_send.encode('utf-8'))

        received_data = client.recv(1024)
        received_json = json.loads(received_data.decode('utf-8'))
        print("Received JSON data from client:", received_json)

        with open('server_received_dummy.json', 'w') as file:
            json.dump(received_json, file)

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    client.close()

except socket.error as e:
    print(f"Socket error during server setup: {e}")
except Exception as e:
    print(f"An unexpected error occurred during server setup: {e}")

finally:
    server.close()
