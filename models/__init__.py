from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .customer import Customer
# def db_setup(app):
#     app.config.from_object('config')
#     db.app = app
#     db.init_app(app)
#     migrate = Migrate(app, db)
#     return db