"""src/main.py

Keyword arguments:
argument -- description
Return: return_description
"""

from flask import Flask
from flask.blueprints import Blueprint
from flask_migrate import Migrate

import config
import routes
from models import db

server = Flask(__name__)

# database configuration

server.debug = config.application_debug
server.config["SQLALCHEMY_DATABASE_URI"] = config.database_uri
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.database_tracker

db.init_app(server)
db.app = server
migrate = Migrate(server, db)

# blueprint config to register endpoints

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.application_root)

if __name__ == "__main__":
    server.debug = True
    server.run(host=config.application_host, port=config.application_port)
