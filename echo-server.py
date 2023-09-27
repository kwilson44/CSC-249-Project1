# Import the socket and math libraries
import socket
import math

# Define the server's IP address and port number
HOST = "127.0.0.1"
PORT = 65432

# Print a message indicating the server is starting and listening for connections
print("Server is starting - listening for connections at IP", HOST, "and port", PORT)

# Define a function to calculate expressions based on user commands
def calculate_expression(expression):
    try:
        parts = expression.split()
        if len(parts) == 3 and parts[1] == "^":
            base = float(parts[0])
            exponent = float(parts[2])
            result = math.pow(base, exponent)
            return f"The result of {expression} is {result}."
        elif len(parts) == 3 and parts[0] == "root":
            degree = float(parts[1])
            number = float(parts[2])
            result = math.pow(number, 1.0 / degree)
            return f"The {degree}-th root of {number} is {result}."
        else:
            return "Invalid expression format. Use 'calculate base ^ exponent' or 'calculate root degree number'."
    except Exception as e:
        return f"Error: {str(e)}"

# Create a socket object using IPv4 and TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the server's address and port
    s.bind((HOST, PORT))
    # Start listening for incoming connections
    s.listen()
    # Accept a client connection and get the client's address
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break

            # Decode the received data as a string
            message = data.decode('utf-8')
            print(f"Received command from client: '{message}'")

            # Perform actions based on the received message
            if message.startswith("calculate "):
                _, expression = message.split(" ", 1)
                response = calculate_expression(expression)
            else:
                response = "Invalid command."

            # Send the response back to the client after encoding it as bytes
            conn.sendall(response.encode('utf-8'))
            print(f"Sent response to client: '{response}'")

        # Print a message indicating the server is done
        print("Server is done!")


