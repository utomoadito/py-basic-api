from app import app, jsonify
import requests
import os

@app.route('/')
@app.route('/index')
def index():
    return "Za Warudo!"

@app.route('/<string:name>/')
def hello_name(name):
    return "Hello " + name

@app.route('/person/', methods=['GET'])
def person():
    payload = {
        'name':'Jimit',
        'address':'India'
    }
    return jsonify(payload), 200

@app.route('/rajaongkir/province')
def province():
    url = 'https://api.rajaongkir.com/starter/province'
    header = {
        'key': os.environ.get('RAJAONGKIR_API_KEY')
    }
    print(header)
    r = requests.get(url=url, headers=header)
    return r.json()