from flask import Flask, make_response
from lib import *

app = Flask(__name__)


@app.route('/turn-on-desktop')
def turn_on_desktop():
    send_magic_packet('F0-2F-74-18-8E-56')


@app.route('/send-ok')
def send_ok():
    response = make_response("Success", 200)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
