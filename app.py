from flask import Flask, request
import os
import xml.etree.ElementTree as ET
import json
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    print('home')
    return '200 ok'

@app.route('/inbound/', methods=['GET', 'POST'])
def inbound():
    print('inbound')
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

@app.route('/push', methods=['GET', 'POST'])
def push():
    print('push')
    if request.method == 'POST':
        return '200 ok'

    if request.method == 'GET':
        print('push-GET')
        res = []
        for key, val in request.args.items():
            res.append((key, val))

        print(res)
    
    return str(res)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', debug=True, port=8080)
    # print(port)
    # sock.close()