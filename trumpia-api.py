from flask import Flask, request
import xml.etree.ElementTree as ET
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def home():
    return '200 ok'

@app.route('/inbound', methods=['GET', 'POST'])

def inbound():
    if request.method == 'POST':
        return '200 ok'

    if request.method == 'GET':
        if 'xml' not in request.args:
            pass
        else:
            response = request.args.get('xml')
            root = ET.fromstring()
            for child in root:
                print(child.tag)
                print(child.text)
        return ''


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    sock.close()
    app.run(debug=True, port = port)