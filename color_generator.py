import random
import zmq


def generate_random_color():
    # Setup ZeroMQ with REP socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://localhost:5558")

    while True:
        # Wait for the next request from the client
        message = socket.recv_string()
        if message == "request_color":
            # Generate a random color and send it back
            color_hex = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            socket.send_string(color_hex)
        else:
            socket.send_string("Unknown request")


if __name__ == "__main__":
    generate_random_color()