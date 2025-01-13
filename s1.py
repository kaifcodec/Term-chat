import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = {}
        self.lock = threading.Lock()

    def broadcast(self, message, exclude_client=None):
        """Broadcast a message to all connected clients except the excluded one."""
        with self.lock:  # Prevent race conditions
            for client in list(self.clients.keys()):
                if client != exclude_client:
                    try:
                        client.send(message.encode("utf-8"))  # Ensure message is encoded to UTF-8
                    except UnicodeEncodeError:
                        print(f"Error encoding message for {client}")
                        self.remove_client(client)
                    except Exception as e:
                        print(f"Error sending message to {client}: {e}")
                        self.remove_client(client)

    def handle_client(self, client_socket, client_address):
        """Handle client communication."""
        try:
            while True:
                # Receive the message
                message = client_socket.recv(1024)
                if not message:
                    break

                # Attempt to decode the message
                try:
                    decoded_message = message.decode("utf-8")
                    if decoded_message.startswith("#file"):  # Check if it's a file header
                        self.handle_file_transfer(client_socket, decoded_message)
                    else:
                        self.broadcast(decoded_message, exclude_client=client_socket)
                except UnicodeDecodeError:
                    print(f"Error decoding message from {client_address}")
                    continue  # Skip this message if it can't be decoded
        except Exception as e:
            print(f"Error with client {client_address}: {e}")
        finally:
            self.remove_client(client_socket)

    def handle_file_transfer(self, client_socket, header):
        """Handle file transfer from client."""
        try:
            # Parse file metadata from the header
            _, file_name, file_size = header.split("|")
            file_size = int(file_size)

            # Receive file data
            file_data = b""
            while len(file_data) < file_size:
                chunk = client_socket.recv(min(file_size - len(file_data), 1024))
                if not chunk:
                    raise ConnectionError("File transfer interrupted.")
                file_data += chunk

            # Save the received file
            with open(f"/storage/emulated/0/Download/{file_name}", "wb") as file:
                file.write(file_data)

            print(f"Received file: {file_name} ({len(file_data)} bytes)")
            self.broadcast(f"{file_name} has been received.", exclude_client=client_socket)

        except Exception as e:
            print(f"Error during file transfer: {e}")
            self.broadcast(f"Error receiving file.", exclude_client=client_socket)

    def remove_client(self, client_socket):
        """Remove a client from the server."""
        with self.lock:
            client_socket.close()
            self.clients.pop(client_socket, None)

    def accept_connections(self):
        """Accept new client connections."""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            self.clients[client_socket] = client_address
            threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()

    def run(self):
        """Start the server."""
        self.accept_connections()

if __name__ == "__main__":
    host = "0.0.0.0"  # Listen on all available interfaces
    port = 5020
    chat_server = ChatServer(host, port)
    chat_server.run()
