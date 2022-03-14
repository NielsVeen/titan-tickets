from flask import Flask,request,json
from dbapp import upload_to_db
app = Flask(__name__)

@app.route("/")
def home():
    return "Webhook is working!"

@app.route('/webhook',methods=['POST'])
def webhook():
    data = request.json
    if data['page'] == "https://tickets.titanmaker.io/lesson/lesson-1/":
        submit_id = data['submit_id']
        email = data['email']
        cro_address = data['cro_address']
        ip_address = data['ip']
        print('check with db')
        db = upload_to_db(submit_id,email,cro_address,ip_address)

        if db == True:
            # Code you want to run if the record does not exist
            print('hello')
        else:
            # Code that runs if record already exists
            print('nice')
        return 'success', 200
    else: return 'error', 404


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)