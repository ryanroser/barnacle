# controllers.py

# Import flask dependencies
from flask import Blueprint, request, render_template, jsonify, json

from .models import greet_user

# Import password / encryption helper tools
# from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
# from app import db

# Import module forms
# from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
# from app.mod_auth.models import User

# Define the blueprint: 'module_one'
module_one = Blueprint('module_one', __name__, template_folder="templates")

# Set the route and accepted methods
@module_one.route('/', methods=['GET'])
def index():
    return render_template("module_one/index.html")

@module_one.route('/hi/<visitor_name>', methods=['GET'])
def hi(visitor_name):
    visitor = {
        "name": visitor_name,
        "greeting": greet_user(visitor_name),
    }
    return render_template("module_one/hi.html", visitor=visitor)

@module_one.route('/api/say-hi', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_say_hi():
    """
    A silly example to show how to make an API endpoint
    and check headers and methods
    """
    response = {}

    if request.headers['Content-Type'] == 'text/plain':
        response['text'] = request.data
    elif request.headers['Content-Type'] == 'application/json':
        response['json'] = request.json
    elif request.headers['Content-Type'] == 'application/octet-stream':
        #f = open('./binary', 'wb')
        #f.write(request.data)
        #        f.close()
        response['binary'] = "Received %s of binary data" % len(request.data)
    else:
        return jsonify({"error": "415 Unsupported Media Type",})

    for method in ['GET', 'POST',]:
        if request.method == method:
            response['hi'] = method
            break
    else:
        response['hi'] = 'other methods'

    return jsonify(response)
