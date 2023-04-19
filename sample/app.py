import requests
import time
from flask import Flask, make_response, render_template
from lib import *
import subprocess
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
run_on_connect = None

start_stream = lambda: requests.get('http://192.168.0.13:5000/start-lightning-stream')


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    return render_template("500_generic.html", e=e), 500


@app.route('/send-ok')
def send_ok():
    global run_on_connect
    if run_on_connect:
        attempts = 90
        while attempts > 0:
            try:
                run_on_connect()
                run_on_connect = None
                break
            except requests.exceptions.ConnectionError:
                attempts -= 1
                time.sleep(0.5)

    time.sleep(0.5)
    res = make_response("Success", 200)
    return res        


@app.route('/start-lightning-stream')
def start_lightning_stream():
    global run_on_connect
    try:
        start_stream()
    except requests.exceptions.ConnectionError:
        send_magic_packet('F0-2F-74-18-8E-56')
        run_on_connect = start_stream

@app.route('/update')
def update():
    subprocess.run(["bash ../update.sh"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
