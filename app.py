from flask import Flask, request
import os
from sys import stderr
import xml.etree.ElementTree as ET
import socket
from flask_ngrok import run_with_ngrok

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
            # pass
        else:
            temp = []
            response = request.args.get('xml')
            root = ET.fromstring(response)
            for child in root:
                temp.append((child.tag, child.text))
                print(str(child.tag) + ': ' + str(child.text))
        return str(temp)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    # port = int(os.environ.get('PORT', 80))
    app.run(debug=True, port=8080)
    # print(port)
    sock.close()