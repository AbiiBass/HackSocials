import socket
import threading
import time
from quick_queue import QQueue
import requests
import netifaces

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host_name = socket.gethostname()
#host_ip = socket.gethostbyname(host_name+ ".local")
iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
host_ip = "192.168.137.1"

#host_ip = "192.168.8.168"  # LOCAL ADDRESS
#host_ip = "192.168.137.183"
# host_ip = "" #NGROK ADDRESS
print('HOST IP:', host_ip)

port = 8889
socket_address = (host_ip, port)
server_socket.bind(socket_address)
server_socket.listen()
print("Listening at", socket_address)

qq = QQueue()

phone = "192.168.8.174"
#phone = "192.168.137.171"


def show_client(addr, client_socket):
    try:
        print('CLIENT {} CONNECTED!'.format(addr))
        if client_socket:  # if a client socket exists
            while True:
                packet = client_socket.recv(1024)

                packet_breakdown = packet.decode().split(":")

                if addr[0] not in list_of_address_phone:
                    if packet_breakdown[2] == "phone":
                        list_of_address_phone.append(addr[0])
                        print(list_of_address_phone)

                print(packet)

                if list_of_address_phone:
                    print(packet_breakdown)
                    if "a" in packet_breakdown:
                        print("send")
                        for i in list_of_address_phone:
                            time.sleep(1)
                            list_of_sockets[list_of_address.index(i)].sendall(packet)
                            print("test" + i)
                            # time.sleep(1)
                # if phone in list_of_address:
                #     if "a" in packet_breakdown:
                #         list_of_sockets[list_of_address.index(phone)].sendall(packet)


                if addr[0] in list_of_address_phone:
                    if packet == b'':
                        print(f"PHONE {addr} DISCONNECTED")
                        list_of_sockets.remove(client_socket)
                        str_addr = str(addr[0])
                        list_of_address.remove(str_addr)
                        list_of_address_phone.remove(str_addr)
                        print(list_of_address_phone)
                        print(list_of_address)
                        break
                    time.sleep(5)
                    client_socket.sendall(packet)
                else:
                    client_socket.sendall(packet)


    except Exception as e:
        print(f"CLIENT {addr} DISCONNECTED")
        list_of_sockets.remove(client_socket)
        str_addr = str(addr[0])
        list_of_address.remove(str_addr)
        pass



list_of_address = []
list_of_address_phone = []
list_of_sockets = []


while True:
    client_socket, addr = server_socket.accept()

    if addr[0] not in list_of_address:
        list_of_address.append(addr[0])
        list_of_sockets.append(client_socket)

    print(list_of_address)
    print(list_of_sockets)

    p1 = threading.Thread(target=show_client, args=(addr, client_socket))
    p1.start()
    print("TOTAL CLIENTS ", threading.activeCount() - 1)