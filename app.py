from flask import Flask, Response

app = Flask(__name__)


@app.route('/clients')
def clients():
    string = ''
    with open('clients.json') as f:
        l = f.readlines()
        for line in l:
            string = string + line
    return Response(string, mimetype='application/json')


@app.route('/products')
def products():
    string = ''
    with open('products.json') as f:
        l = f.readlines()
        for line in l:
            string = string + line
    return Response(string, mimetype='application/json')


@app.route('/sales', methods=['POST'])
def sales():
    return Response("{'result': OK}",mimetype='application/json')


@app.route('/on', methods=['POST'])
def ligthon():
    return Response("{'light': 'ON'}", mimetype='application/json')


@app.route('/off', methods=['POST'])
def ligthoff():
    return Response("{'light': 'OFF'}", mimetype='application/json')