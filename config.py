# imports
import datetime
import logging
import os
from dotenv import load_dotenv

load_dotenv()
dbUsername = os.getenv('DB_USERNAME')
dbPassword = os.getenv('DB_PASSWORD')
dbHost = os.getenv('DB_HOST')
dbPort = os.getenv('DB_PORT')
dbName = os.getenv('DB_NAME')

# Enable debug mode.
DEBUG = True

# Connect to development database (POSTGRES)
SQLALCHEMY_DATABASE_URI = f'postgresql://{dbUsername}:{dbPassword}@{dbHost}:{dbPort}/{dbName}'

# # Connect to production database
# SQLALCHEMY_DATABASE_URI = f'postgresql+pg8000://{dbUsername}:{dbPassword}@{dbHost}:{dbPort}/{dbName}'

# # Connect to development database
# # SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg://{dbUsername}:{dbPassword}@{dbHost}:{dbPort}/{dbName}'

SQLALCHEMY_TRACK_MODIFICATIONS = False

if DEBUG:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s: %(message)s",
        datefmt="%d/%m/%y %H:%M:%S",
    )
else:
    filename = datetime.datetime.now().strftime('%d-%m-%Y')
    logging.basicConfig(
        filename=f"logs/{filename}.log",
        level=logging.WARNING,
        format="%(asctime)s %(levelname)s:\
        %(filename)s %(funcName)s \
        pid:%(process)s module:%(module)s %(message)s",
        datefmt="%H:%M:%S",
    )