import socket

# Initialize client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Main loop to send messages
while True:
    message = input("Enter message to send (JOIN <username> or SEND <message>): ")
    if message.lower() == 'exit':
        break
    try:
        client_socket.send(message.encode('utf-8'))

        # Receive response from server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")
    except Exception as e:
        print(f"Error sending/receiving message: {e}")
        break

# Close the connection
client_socket.close()
