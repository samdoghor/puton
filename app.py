import os
from flask import Flask, jsonify, request, Response
from flask_migrate import Migrate
import json

# from models import db_setup
import config
import routes
from models import db

app = Flask(__name__)

# configurations
SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
# db = db_setup(app)

app.debug = config.DEBUG
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS  # noqa
db.init_app(app)
db.app = app
migrate = Migrate(app, db)


""" Error handling """


# error handler for 422
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

# error handler for 400
@app.errorhandler(400)
def bad_request(error):
    print(error)
    return jsonify({
        "success": False,
        "error": 400,
        "message": error.description
    }), 400


# error handler for 401
@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": error.description
    }), 401


# error handler for 403
@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": error.description
    }), 403


# error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": error.description
    }), 404


# error handler for 500
@app.errorhandler(500)
def internal_server_error(error):
    print({"error": error})
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
    }), 500


if __name__ == "__main__":
    app.debug = config.DEBUG
    app.run(host=config.dbHost, port=config.dbPort)

# app.run()