# Bluetooth Socket Communication

This project implements a client-server model using the Python socket library for Bluetooth communication.
The goal is to establish a connection between a server and a client, enabling the exchange of dummy JSON files.

## Files

- server.py: The Python script for the server side of the communication.
- client.py: The Python script for the client side of the communication.

## Prerequisites
- Python 
- Bluetooth-enabled devices (server and client)

### Server
1. Run the server script:
	python server.py
    
2. The server will open a Bluetooth socket and wait for incoming client connections.
3. Upon client connection, the server SEND a JSON file 'server_dummy.json'  TO the client.
4. The server then recieve 'received_json' data from the server, and save it as 'server_received_dummy.json',
 and closes the connection.

### Client
1. Run the client script:

       python client.py
    
2. The client connects to the specified server (change Bluetooth address if needed) and and waits for the server's response.
3. Received JSON data from the server and printed then saved as 'client_received_dummy.json
2. Sends a dummy JSON file to the server.


## Configuration

- Bluetooth address in both scripts is set as a placeholder. Change it to the actual server's Bluetooth address as needed.

## Files

- server.py: Main server script.
- client.py: Main client script.
- client_dummy.json: Dummy JSON file used by the server.
- client_dummy.json: Dummy JSON file used by the client.
- server_received_dummy.json: JSON file where received data from the client is saved on the server.
- client_received_dummy.json: JSON file where received data from the server is saved on the client.

## Troubleshooting

- Handle any FileNotFoundError by ensuring necessary JSON files exist.
- If encountering socket.error, check for any connection issues.

## Credits

- Developed by Yeniyan semman shifa
