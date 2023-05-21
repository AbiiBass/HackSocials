import socket
import threading
import time
from quick_queue import QQueue
import requests

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = socket.gethostname()
# host_ip = socket.gethostbyname(host_name+ ".local")
#host_ip = "192.168.8.168"  # LOCAL ADDRESS
host_ip = "192.168.137.1"
# host_ip = "" #NGROK ADDRESS
print('HOST IP:', host_ip)

port = 8889
socket_address = (host_ip, port)
server_socket.bind(socket_address)
server_socket.listen()
print("Listening at", socket_address)

qq = QQueue()

#phone = "192.168.8.174"
phone = "192.168.137.12"

bear1 = "192.168.8.190"
bear2 = "192.168.8.140"


def show_client(addr, client_socket):
    try:
        print('CLIENT {} CONNECTED!'.format(addr))
        if client_socket:  # if a client socket exists
            while True:
                packet = client_socket.recv(1024)
                packet_breakdown = packet.decode().split(":")
                print(packet)
                if phone in list_of_address:
                    if "a" in packet_breakdown:
                        list_of_sockets[list_of_address.index(phone)].sendall(packet)
                        #list_of_sockets[list_of_address.index("192.168.137.171")].sendall(packet)
                if addr[0] == phone:
                    if packet == b'':
                        print(f"PHONE {addr} DISCONNECTED")
                        list_of_sockets.remove(client_socket)
                        str_addr = str(addr)
                        print(str_addr[2:17])
                        list_of_address.remove(str(str_addr[2:17]))
                        break
                    time.sleep(5)
                    client_socket.sendall(packet)
                else:
                    client_socket.sendall(packet)




                # data_to_send = str(addr) + str(packet.decode())
                # put_to_queue(data_to_send)
                # client_socket.sendall(packet)


    except Exception as e:
        print(f"CLIENT {addr} DISCONNECTED")
        list_of_sockets.remove(client_socket)
        str_addr = str(addr)
        print(str_addr[2:17])
        list_of_address.remove(str(str_addr[2:17]))
        pass


def put_to_queue(data_in):
    qq.put_bucket(data_in)
    print("data from qq:" + qq.get_bucket())


list_of_address = []
list_of_sockets = []

BASE = "https://3ff2-101-78-74-189.ap.ngrok.io/"


def split_string(data):
    str_i = str(data)
    temp = str_i.split(", ")
    temp1 = temp[6] + temp[7]
    address = temp1[8:23]
    port = temp1[22:27]
    if address not in list_of_address:
        list_of_address.append(address)
        list_of_sockets.append(data)
        # response = requests.put(BASE + "bearaddress/7362/",
        #                         {"address": address,
        #                          "name": ""})
        # print(response)


while True:
    client_socket, addr = server_socket.accept()

    split_string(client_socket)
    print(list_of_address)
    print(list_of_sockets)

    p1 = threading.Thread(target=show_client, args=(addr, client_socket))
    p1.start()
    print("TOTAL CLIENTS ", threading.activeCount() - 1)
