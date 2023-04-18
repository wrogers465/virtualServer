from flask import Flask, jsonify
from lib import *


app = Flask(__name__)

@app.route('/turn-on-desktop')
def turn_on_desktop():
    send_magic_packet('F0-2F-74-18-8E-56')
    store_run_time()

@app.route('/get-last-run-time', methods=['GET'])
def get_last_run_time():
    data = get_run_time()

    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
