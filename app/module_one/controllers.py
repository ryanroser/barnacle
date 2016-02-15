# controllers.py

# Import flask dependencies
from flask import Blueprint, request, render_template, abort
from flask_restful import Api, Resource, reqparse

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
# And create the flask-restful API
module_one_api = Api(module_one)

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

# API Controllers

class SayHi(Resource):
    """
    A silly example to show how to make an API endpoint
    and check headers and methods
    """

    def get(self):
        return "Hi!"

    def post(self):
        # parse args
        args = self.parser.parse_args()
        content_type = args.get("Content-Type")

        if content_type != "application/json":
            abort(415)

        response = {}
        response["hi"] = "POST"
        response['json'] = request.json

        return response

    def __init__(self, *args, **kwargs):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('Content-Type', location='headers')
        super(SayHi, self).__init__(*args, **kwargs)

module_one_api.add_resource(SayHi, "/api/say-hi")
