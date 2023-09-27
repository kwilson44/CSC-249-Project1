import socket

HOST = "127.0.0.1"
PORT = 65432

print("Client starting - connecting to server at IP", HOST, "and port", PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to the server.")

    # Prompt the user for input
    while True:
        print("Available commands:")
        print("1. calculate base ^ exponent - Calculate base raised to the exponent.")
        print("2. calculate root degree number - Calculate the nth root of a number.")
        print("3. quit - Quit the client.")
        print("Enter commands like 'calculate 2 ^ 3' or 'calculate root 3 27'. ")
        command = input("Enter a command: ")

        if command == "quit":
            break

        s.sendall(command.encode('utf-8'))
        print(f"Sent command to server: '{command}'")

        data = s.recv(1024)
        print(f"Received response from the server: '{data.decode('utf-8')}'")

print("Client is done!")
#