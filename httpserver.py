import socket
import argparse
import threading
import sys
from serverlibrary import *


def run_server(host, port):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        listener.bind((host, port))
        listener.listen(5)
        print('Server is listening at port: ', port)
        while True:
            conn, addr = listener.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
    finally:
        listener.close()


def handle_client(conn, addr):
    print('New client from', addr)
    data = conn.recv(1024)
    print("data received from client: ", data.decode("utf-8"))
    data = process_request(data)
    conn.sendall(data.encode())
    conn.close()


parser = argparse.ArgumentParser()
parser.add_argument("--port", help="HTTP server post", type=int, default=8000)
args = parser.parse_args()
run_server('', args.port)
