from flask import Flask, request
import os
from sys import stderr
import xml.etree.ElementTree as ET
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    print('home', file=stderr)
    return '200 ok'

@app.route('/inbound/', methods=['GET', 'POST'])
def inbound():
    print('inbound', file=stderr)
    if request.method == 'POST':
        return '200 ok'

    if request.method == 'GET':
        if 'xml' not in request.args: 
            return 'NO XML'
            pass
        else:
            response = request.args.get('xml')
            root = ET.fromstring(response)
            for child in root:
                print(str(child.tag) + ': ' + str(child.text)
        return 'GET'


if __name__ == '__main__':
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind(('localhost', 0))
    # port = sock.getsockname()[1]
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True, port=port)
    # print(port)
    # sock.close()