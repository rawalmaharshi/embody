import string
import random

from flask import Flask, request
from flask import request
from flask import jsonify
import redis

app = Flask(__name__)

r = redis.Redis(host='db', port=6379, db=0)

@app.route('/ping', methods=['GET'])
def ping():
    return 'PONG', 200

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/getuserkey', methods=['GET'])
def user_key():
    user_id = request.args.to_dict()['user_id']
    cached_key =  r.get(user_id)
    if cached_key is None :     #enter user id in cache
        #generate random user key of length 16
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        r.set(user_id, res)
        cached_key = res
    else :
        cached_key = cached_key.decode('utf-8')
    
    return jsonify(
        user_key=cached_key,
        port_number=5001
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)