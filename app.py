from flask import Flask,request,jsonify,json
from database import database
from send import send_cro
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Homepage'

@app.route('/post',methods=['POST'])
def post():
    if request.json:
        data = request.json

        # Create variables from request data
        submission_id = data['submit_id']
        email = data['email']
        cro_address = data['cro_address']
        ip_address = data['ip']

        # Run database function
        db = database(submission_id,email,cro_address,ip_address)

        if db == True:
            print('sending funds')
            send_cro(data['cro_address'])
            print('funds sent')
            return 'nice it worked',200
        else:
            return 'something wrong with data', 200
    return 'no data',404

if __name__ == '__main__':
    app.run(threaded=True,port=5000)