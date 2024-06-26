import socket
import select


def send_request(request, host='localhost', send_port=4332, receive_port=5100):
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        send_socket.connect((host, send_port))
        send_socket.sendall(request.encode())
        send_socket.close()
    except ConnectionRefusedError:
        print(f"The connection to the server was terminated:(")
        return

    receive_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receive_socket.bind((host, receive_port))
    receive_socket.listen(1)

    print("Expect response from server...")

    # Используем select для ожидания данных с receive_socket
    ready_sockets, _, _ = select.select([receive_socket], [], [], 3)

    if ready_sockets:
        connection, addr = receive_socket.accept()
        with connection:
            data = connection.recv(1024)
            if data:
                print("Get response :", data.decode())
            else:
                print("Response is empty")
    else:
        print("Xm... No data on port -", receive_port)

    receive_socket.close()


if __name__ == "__main__":
    while True:
        request = input("Write request :\n")
        send_request(request)