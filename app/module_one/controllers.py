# controllers.py

# Import flask dependencies
from flask import Blueprint, request, render_template, abort
from flask_restplus import Api, Resource, reqparse, fields

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


#### Web Controllers ###

# Set the route and accepted methods
@module_one.route('/', methods=['GET'])
def index():
    return render_template("module_one/index.html", visitors=["Tim", "John", "Becky"])

@module_one.route('/hi/<visitor_name>', methods=['GET'])
def hi(visitor_name):
    visitor = {
        "name": visitor_name,
        "greeting": greet_user(visitor_name),
    }
    return render_template("module_one/hi.html", visitor=visitor)


### API Controllers ###

# And create the flask-restplus API
api = Api(module_one, doc='/doc/',
    version='1.0', title='Module One API',
    description="""\
This is the API for Module One. It does the following:

* Records greetings for users given by user name
* Looks up the greeting for a user given by user name
""")

# This is the route namespace for the API
ns = api.namespace("api", description="Module One API")

# Describe the model used by the API
m1 = api.model("Module One", {
    "user_name": fields.String(required=True, description="The name of the user"),
    "greeting": fields.String(description="A specific greeting for a user"),
})

# the data store :)
class UserGreetings(dict):
    def validate(self, data):
        if "user_name" not in data:
            abort(400, "Invalid request")
user_greetings = UserGreetings()


@ns.route("/greetings")
class GreetingList(Resource):
    """
    Shows a list of all greetings and allows you to POST a new greeting
    """
    @ns.doc("list_greetings")
    @ns.marshal_list_with(m1)
    def get(self):
        """List all greetings"""
        print user_greetings.values()
        return user_greetings.values()

    @ns.doc("create_greeting")
    @ns.expect(m1)
    @ns.marshal_with(m1, code=201)
    def post(self):
        """Create a new greeting"""
        ug = api.payload
        user_greetings.validate(ug)
        user_greetings[ug["user_name"]] = ug
        return user_greetings[ug["user_name"]], 201


@ns.route("/greetings/<string:user_name>/")
@ns.response(404, "Greeting not found")
@ns.param("user_name", "the user's name")
class Greeting(Resource):
    """Show a single greeting and delete a greeting"""
    @ns.doc("get_greeting")
    @ns.marshal_with(m1)
    def get(self, user_name):
        """Fetch a greeting"""
        try:
            return user_greetings[user_name]
        except:
            abort(404)

    @ns.doc("delete_greeting")
    @ns.response(204, "Greeting deleted")
    def delete(self, user_name):
        """Delete a greeting for a user name"""
        try:
            user_greetings.pop(user_name)
            return "", 204
        except KeyError:
            abort(404)

    @ns.doc("put_greeting")
    @ns.expect(m1)
    @ns.marshal_with(m1)
    def put(self, user_name):
        """Updates a greeting for a user"""
        data = api.payload
        data["user_name"] = user_name
        user_greetings.validate(data)
        user_greetings[user_name] = data
        return user_greetings[user_name]
