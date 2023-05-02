import socket
import sqlite3


DB_PATH = "./data.db"


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


def get_items_in_container(container: str) -> list:
    container = container.lower()
    with sqlite3.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT item_name FROM inventory WHERE container = ?", (container,))
        return [ row[0] for row in cur.fetchall() ]
    

def find_item(item_name: str) -> list:
    item_name = item_name.lower()
    with sqlite3.connect(DB_PATH) as db:
        results = None
        cur = db.cursor()
        cur.execute("SELECT item_name, container FROM inventory WHERE item_name = ?", (item_name,))
        results = cur.fetchone()
        if not results:
            split_item_name = item_name.split(" ")
            if len(split_item_name) == 1:
                split_item_name = item_name.split("-")
            for partial_name in split_item_name:
                cur.execute("SELECT item_name, container FROM inventory WHERE instr(item_name, ?) OR instr(tags, ?) LIMIT 3", (partial_name, partial_name,))
                results = cur.fetchall()
                if len(results) > 0:
                    break

        return results


def create_db():
    with sqlite3.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("CREATE TABLE inventory (uuid TEXT UNIQUE, item_name TEXT UNIQUE, container TEXT, tags TEXT)")
        db.commit()