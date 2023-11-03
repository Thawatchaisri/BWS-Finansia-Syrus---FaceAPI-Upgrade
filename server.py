from flask import Flask, request, Blueprint, send_from_directory
import os
from login_check import login_check as lc
from register_on_submit import register_on_submit as rs

# The line `main = Blueprint('main', __name__)` creates a Blueprint object named 'main'. A Blueprint
# is a way to organize and group related routes and views in a Flask application. It allows you to
# define routes and views in separate modules and then register them with the main Flask application.
main = Blueprint('main', __name__)

secret_key = str(os.urandom(24))

# The code `app = Flask(__name__)` creates a Flask application object. The `__name__` argument is a
# special Python variable that represents the name of the current module.
app = Flask(__name__)
app.config['TESTING'] = False
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'deployment'
app.config['SECRET_KEY'] = secret_key

app.register_blueprint(main)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    The function "index" returns the string "Online".
    :return: the string "Online".
    """
    return "Online"

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    The function `register` takes in a JSON object containing a URL and a UID, and returns the status of
    a function `rs` with the UID and URL as arguments.
    :return: the value of the variable "status".
    """
    request_data = request.json
    url,uid = request_data['url'],request_data['uid']

    status = rs(uid,url)
    return status

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    The `login` function takes in a JSON object containing a URL and a UID, and returns the status of a
    function call `lc` with the UID and URL as arguments.
    :return: The status variable is being returned.
    """
    request_data = request.json
    url,uid = request_data['url'],request_data['uid']

    status = lc(uid,url)
    return status

@app.route('/chkregister', methods=['GET', 'POST'])
def chkregister():
    """
    The function `chkregister()` checks if a file with the name 'uid.png' exists in the 'student'
    directory and returns 'valid' if it exists, otherwise it returns 'invalid'.
    :return: either 'valid' or 'invalid' based on the existence of a file with the name 'uid.png' in the
    'student' directory.
    """
    request_data = request.json
    request_data,uid = request.json,request_data['uid']

    valid = os.path.exists('student/'+uid+'.png')

    if(valid):
        return 'valid'
    else:
        return 'invalid'
   



@app.route('/favicon.ico') 
def favicon(): 
    """
    The function `favicon` returns the favicon.ico file from the static directory.
    :return: the favicon.ico file from the static directory with the mimetype
    'image/vnd.microsoft.icon'.
    """
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# The `if __name__ == "__main__":` block is used to ensure that the Flask application is only run if
# the script is executed directly, and not imported as a module.
if __name__ == "__main__":
    app.run(debug=False,port=5000)
