import requests
import time
from flask import Flask, make_response
from lib import *

app = Flask(__name__)
run_on_connect = None

start_stream = lambda: requests.get('http://192.168.0.13:5000/start-lightning-stream')


@app.route('/send-ok')
def send_ok():
    if run_on_connect:
        attempts = 90
        while attempts > 0:
            try:
                run_on_connect()
                break
            except requests.exceptions.ConnectionError:
                attempts -= 1
                time.sleep(0.5)


@app.route('/run-instructions')
def run_instructions():
    global run_on_connect
    if run_on_connect:
        run_on_connect()
        run_on_connect = None
    else:
        response = make_response("No instructions to run", 200)
        return response


@app.route('/start-lightning-stream')
def start_lightning_stream():
    global run_on_connect
    try:
        start_stream()
    except requests.exceptions.ConnectionError:
        send_magic_packet('F0-2F-74-18-8E-56')
        run_on_connect = start_stream

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
