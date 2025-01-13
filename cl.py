import socket
import threading
import textwrap  # To wrap long messages into multiple lines
from colorama import Fore, init
import os  # For file operations

# Initialize colorama
init(autoreset=True)

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = None
        self.nickname = None
        self.first_prompt = True  # Flag to show the prompt only once
        self.header_size = 64  # Fixed header size in bytes

    def connect(self):
        """Connect to the chat server."""
        if self.client:  # Close the existing socket if it's already open
            self.client.close()

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.nickname = input(Fore.YELLOW + "Choose a nickname: ")
        self.client.send(self.nickname.encode("utf-8"))

    def receive_messages(self):
        """Receive and display messages from the server."""
        while True:
            try:
                message = self.client.recv(1024)  # Receive the message
                if not message:
                    raise ConnectionError("Disconnected from server.")
                decoded_message = message.decode("utf-8")  # Decode message
                if decoded_message.startswith("#file"):  # Check if it's a file header
                    self.receive_file(decoded_message)
                else:
                    self.display_message_in_box(decoded_message, sender=True)
            except UnicodeDecodeError:
                print(Fore.RED + "Error decoding message. Skipping message.")
                continue
            except ConnectionError as e:
                print(Fore.RED + f"Connection error: {e}")
                break
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}")
                break

    def receive_file(self, header):
        """Handle receiving a file."""
        try:
            _, file_name, file_size = header.split("|")
            file_size = int(file_size)

            # Receive file data
            file_data = b""
            while len(file_data) < file_size:
                chunk = self.client.recv(min(file_size - len(file_data), 1024))
                if not chunk:
                    raise ConnectionError("File transfer interrupted.")
                file_data += chunk

            # Save the file temporarily in the current directory
            with open(file_name, "wb") as file:
                file.write(file_data)

            # Move the file to /storage/emulated/0/Download
            os.system(f"mv {file_name} /storage/emulated/0/Download/")

            print(Fore.GREEN + f"Received file saved to: /storage/emulated/0/Download/{file_name}")
        except Exception as e:
            print(Fore.RED + f"Error receiving file: {e}")

    def display_message_in_box(self, message, sender):
        """Display a message inside a box with multi-line support."""
        terminal_width = 80  # Adjust to your terminal width
        max_msg_width = terminal_width - 20

        # Wrap long messages into multiple lines
        wrapped_lines = textwrap.wrap(message, width=max_msg_width)

        # Calculate box width (same for sender and user)
        box_width = max(len(line) for line in wrapped_lines) + 2

        if sender:
            # Sender's message on the left
            border = Fore.GREEN + f"+{'-' * box_width}+"
            print("\n" + border)
            for line in wrapped_lines:
                print(Fore.GREEN + f"| {line.ljust(box_width - 2)} |")  # Left-align lines
            print(border)
        else:
            # Your message on the right
            spaces = ' ' * (terminal_width - box_width - 4)
            border = Fore.YELLOW + f"{spaces}+{'-' * box_width}+"
            print("\n" + border)
            for line in wrapped_lines:
                print(Fore.YELLOW + f"{spaces}| {line.ljust(box_width - 2)} |")  # Right-align lines
            print(border)

    def send_messages(self):
        """Send messages or files to the server."""
        while True:
            if self.first_prompt:
                print(Fore.CYAN + "You can type a message or use #file to send a file.")
                self.first_prompt = False

            try:
                message = input("").strip()

                if self.client.fileno() == -1:  # Check if the socket is still open
                    print(Fore.RED + "Connection lost. Reconnecting...")
                    self.connect()  # Reconnect if socket is closed

                if message == "#file":
                    file_path = input(Fore.BLUE + "Enter the file path: ").strip()
                    try:
                        with open(file_path, "rb") as file:
                            file_data = file.read()
                        file_name = file_path.split("/")[-1]
                        file_size = len(file_data)
                        header = f"#file|{file_name}|{file_size}".ljust(self.header_size)
                        self.client.send(header.encode("utf-8"))  # Send fixed-size header
                        self.client.sendall(file_data)  # Send the file
                        print(Fore.GREEN + f"File '{file_name}' sent successfully.")
                    except FileNotFoundError:
                        print(Fore.RED + "File not found. Please try again.")
                else:
                    formatted_message = f"{self.nickname}: {message}".ljust(self.header_size)
                    self.client.send(formatted_message.encode("utf-8"))

                    # Clear the input line from the terminal after sending
                    print("\033[A                             \033[A", end="\r")
                    self.display_message_in_box(f"You: {message}", sender=False)

            except Exception as e:
                print(Fore.RED + f"Error sending message: {e}")
                continue  # Continue to next iteration if there's an error

    def run(self):
        """Run the client."""
        try:
            self.connect()
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()
            self.send_messages()
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")
        finally:
            if self.client:
                self.client.close()

if __name__ == "__main__":
    HOST = input(Fore.YELLOW + "Enter server IP: ").strip()
    PORT = int(input(Fore.YELLOW + "Enter server port: ").strip())

    chat_client = ChatClient(HOST, PORT)
    chat_client.run()
