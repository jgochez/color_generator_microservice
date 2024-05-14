import zmq


def random_color_generator():
    # Set up ZeroMQ with REQ socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5557")

    # Main loop to send requests and receive responses
    while True:
        run = input("Press <enter> to generate random color or type 'exit' to quit: ")
        if run.lower() == 'exit':
            break

        # Send a request
        socket.send_string("request_color")

        # Receive the response containing the color hex
        color_hex = socket.recv_string()
        if color_hex:
            msg = f"Received color: {color_hex}"
            print(msg)


if __name__ == "__main__":
    random_color_generator()
