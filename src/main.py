"""
The
"""
from flask import Blueprint, Flask, jsonify, request
from flask_migrate import Migrate

import app
import config
from models import db

# configurations
main = Flask(__name__)
main.config['SECRET_KEY'] = config.SECRET_KEY

main.debug = config.DEBUG
main.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
main.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS  # noqa E501
db.init_app(main)
db.app = main
migrate = Migrate(main, db)

for blueprint in vars(app).values():
    if isinstance(blueprint, Blueprint):
        main.register_blueprint(
            blueprint)

# homepage


@main.route('/')
def index():
    """ Confirms and displays basic info that the main is running """

    main_details = []

    main_details = jsonify({
        "App Name": "MSB App",
        "Current URL": f"{request.url}",
        "Endpoints Access": "http://127.0.0.1:3303/",
        "Message": "The app is up and running",
        "Version": "1.0.0"
    })

    return main_details


if __name__ == "__main__":
    main.debug = config.DEBUG
    main.run(host=config.HOST, port=config.PORT)
