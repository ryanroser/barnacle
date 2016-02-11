# Import flask dependencies
from flask import Blueprint, request, render_template

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
    visitor = {"name": visitor_name,}
    if len(visitor_name) % 2 == 0:
        visitor["greeting"] = "Nice to see you!"
    else:
        visitor["greeting"] = "Thanks for visiting!"
    return render_template("module_one/hi.html", visitor=visitor)
