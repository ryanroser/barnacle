# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# For Dev/Prod config changes, load a config file from a path
# specified by an environment variable.
# See: http://flask.pocoo.org/docs/0.10/config/
# app.config.from_envvar("PATH_TO_CONFIG_FILE")

# Define the database object which is imported
# by modules and controllers
# db = SQLAlchemy(app)

# Sample HTTP error handling
# from flask import render_template
# @app.errorhandler(404)
# def not_found(error):
#    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from .module_one.controllers import module_one

# Register blueprint(s), set their url prefixes: app.url/prefix
app.register_blueprint(module_one, url_prefix='/m1')

# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()
