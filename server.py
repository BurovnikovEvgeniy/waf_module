import re
import socket
import threading


def load_cheat_sheet(file_path):
    cheat_sheet = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            cheat_sheet = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode file '{file_path}' using UTF-8 encoding.")
    except Exception as e:
        print(f"An error occurred while loading cheat sheet file: {e}")
    return cheat_sheet


def check_sql_injection(input_str, cheat_sheet):
    if not cheat_sheet:
        return False

    for pattern in cheat_sheet:
        if re.search(pattern, input_str, re.IGNORECASE):
            return True
    return False


def normalize_query(query):
    normalized_query = query.strip()
    normalized_query = re.sub(r'\s+', ' ', normalized_query)
    return normalized_query


def receive_data():
    # Создаем сокет для приема данных
    receive_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 4332
    receive_socket.bind(('0.0.0.0', port))
    receive_socket.listen(1)
    print("The server is listening on port " + str(port) + "...\n")

    while True:
        conn, addr = receive_socket.accept()
        print(f"The connection is established with {addr}")

        query = conn.recv(1024).decode('utf-8')
        if not query:
            break
        print(f"Data received: {query}")

        normalized_query = normalize_query(query)
        cheat_sheet_file = 'static/cheat_sheet.txt'
        cheat_sheet = load_cheat_sheet(cheat_sheet_file)

        if check_sql_injection(normalized_query, cheat_sheet):
            print(f"SQL Injection detected! Query - \"" + query + "\" was blocked!\n")
        else:
            print(f"The data is safe. sends a response\n")
            send_data(query)

        conn.close()


def send_data(data):
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_socket.connect(('127.0.0.1', 5100))
    send_socket.sendall(data.encode('utf-8'))
    send_socket.close()


if __name__ == '__main__':
    receive_thread = threading.Thread(target=receive_data)
    receive_thread.start()
