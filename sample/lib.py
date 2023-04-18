import json
import socket
import time


def send_magic_packet(mac_address, broadcast_address='255.255.255.255', port=9):
    # Convert the MAC address string to a byte array
    bytes_mac = bytes.fromhex(mac_address.replace('-', ''))

    # Create the magic packet: 6 bytes of FF followed by the MAC address repeated 16 times
    magic_packet = b'\xFF' * 6 + bytes_mac * 16

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Enable broadcasting for the socket
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Send the magic packet to the broadcast address using the specified port (default is 9)
        sock.sendto(magic_packet, (broadcast_address, port))

def store_run_time():
    data = {'last_run_time': time.time()}
    with open('data.json', 'w') as f:
        json.dump(data, f)

def get_run_time():
    with open('data.json', 'r') as f:
        data = json.load(f)

    return data


if __name__ == '__main__':
    pass