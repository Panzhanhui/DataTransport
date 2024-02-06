
import os
import socket
import time

status = False


def send_message(client_socket, message):
    client_socket.send(message.encode('utf-8'))


def receive_response(client_socket):
    response, server_address = client_socket.recvfrom(1024)
    print(
        f"Received response from server at {server_address}: {response.decode('utf-8')}")
    return (server_address, response.decode('utf-8'))


def recordIP(host):
    h = 'host.txt'

    with open(h, 'w', encoding='utf-8') as f:
        f.write(host)


def test():
    global status
    server_host = '255.255.255.255'  # 广播地址
    server_port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try:
        while True:
            message = 1
            server_address = (server_host, server_port)
            send_message(client_socket, message, server_address)
            host, msg = receive_response(client_socket)
            if msg is '101':
                status = True
                recordIP(host)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Client stopped.")
    finally:
        client_socket.close()


def start(server_host, server_port, msg):

    if status:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((server_host, server_port))

            while True:
                message = msg
                send_message(client_socket, message)
                time.sleep(1)
        except socket.error as e:
            print(f"Failed to connect to server: {e}")
        except KeyboardInterrupt:
            print("Client stopped.")
        finally:
            client_socket.close()
    else:
        print('no slave machine')
