import socket
import subprocess
from flask import Flask


app = Flask(__name__)

@app.route('/turn-on-desktop')
def run_script():
    turn_on_desktop('F0-2F-74-18-8E-56')

def turn_on_desktop(mac_address, broadcast_address='255.255.255.255', port=9):
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

if __name__ == '__main__':
    turn_on_desktop('F0-2F-74-18-8E-56')
    #app.run(host='0.0.0.0', port=5000)
