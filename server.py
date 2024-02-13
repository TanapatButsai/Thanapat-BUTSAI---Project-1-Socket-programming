import socket

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")
    username = None

    while True:
        # Receive data from client
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received message from {address}: {data}")

            # Parse request
            parts = data.split()
            if parts[0] == 'JOIN':
                username = parts[1]
                response = "200 OK"
            elif parts[0] == 'SEND':
                if username:
                    message = ' '.join(parts[1:])
                    print(f"{username}: {message}")
                    response = "200 OK"
                else:
                    response = "401 Unauthorized"
            else:
                response = "400 Bad Request"

            # Send response to client
            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"Error receiving message from {address}: {e}")
            break

    print(f"Connection from {address} closed.")
    client_socket.close()

# Initialize server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up server address and port
server_address = ('localhost', 12345)

# Bind server to address and port
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

print("Server is listening...")

# Main server loop
while True:
    # Accept incoming connection
    client_socket, address = server.accept()

    # Create a new thread to handle the client
    handle_client(client_socket, address)
