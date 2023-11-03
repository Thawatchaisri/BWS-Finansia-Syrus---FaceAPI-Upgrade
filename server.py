from flask import Flask, request, Blueprint, send_from_directory
import os
from login_check import login_check as lc
from register_on_submit import register_on_submit as rs


main = Blueprint('main', __name__)

secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = False
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'deployment'
app.config['SECRET_KEY'] = secret_key

app.register_blueprint(main)

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello, World!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    request_data = request.json
    url,uid = request_data['url'],request_data['uid']


    status = rs(uid,url)
    return status

@app.route('/login', methods=['GET', 'POST'])
def login():
    request_data = request.json
    url,uid = request_data['url'],request_data['uid']

    status = lc(uid,url)
    return status

@app.route('/chkregister', methods=['GET', 'POST'])
def chkregister():
    request_data = request.json
    request_data,uid = request.json,request_data['uid']

    valid = os.path.exists('student/'+uid+'.png')

    if(valid):
        return 'valid'
    else:
        return 'invalid'
   



@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=False,port=5000)
