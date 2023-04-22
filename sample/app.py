import requests
import time

import subprocess
from flask import Flask, make_response
from lib import *


app = Flask(__name__)
run_on_connect = None

start_stream = lambda: requests.get('http://192.168.0.13:5000/start-lightning-stream')


@app.route('/get-instructions')
def send_instructions():
    global run_on_connect
    content = "Ok from server http://192.168.0.2:5000"
    if run_on_connect:
        content += ". Run {run_on_connect}"
        run_on_connect = None

    res = make_response(content, 200)
    return res        


@app.route('/start-lightning-stream')
def start_lightning_stream():
    global run_on_connect
    try:
        start_stream()
    except requests.exceptions.ConnectionError:
        send_magic_packet('F0-2F-74-18-8E-56')
        run_on_connect = "start-lightning-stream"

@app.route('/update')
def update():
    subprocess.call(["/home/pi/Python/Projects/virtualServer/update.sh"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
