
from flask import Blueprint, Flask, jsonify, request
from flask_migrate import Migrate

import config
import app
from models import db

# configurations
server = Flask(__name__)
server.config['SECRET_KEY'] = config.SECRET_KEY

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(server)
db.app = server
migrate = Migrate(server, db)

for blueprint in vars(app).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint)

# homepage


@server.route('/')
def index():
    """ Confirms and displays basic info that the server is runnign """

    server = jsonify({
        "App Name": "MSB App",
        "Current URL": f"{request.url}",
        "Endpoints Access": "http://127.0.0.1:3303/[endpoints]",
        "Message": "The server is up and running",
        "Version": "1.0.0"
    })

    return server


if __name__ == "__main__":
    server.debug = config.DEBUG
    server.run(host=config.HOST, port=config.PORT)
