import string
import random
import redis

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

# Redis Connection
r = redis.Redis(host='db', port=6379, db=0)

#Route for /
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


#Route for /ping - testing
@app.route('/ping', methods=['GET'])
def ping():
    return 'PONG'


#Route to get the user key for a particular user id
@app.route('/getuserkey', methods=['GET'])
def user_key():
    user_id = request.args.to_dict()['user_id']
    cached_key =  r.get(user_id)
    # check if passesd user id in db or not
    if cached_key is None :
        #generate random user key of length 32
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
        #set in redis db
        r.set(user_id, res)
        #return value
        cached_key = res
    else :
        #if key is present, decode it from bytes
        cached_key = cached_key.decode('utf-8')

    #return response
    return jsonify(
        user_key=cached_key,
        port_number=5003
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)