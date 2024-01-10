"""
Thes
"""

# imports

import datetime
import logging
import os

from dotenv import load_dotenv

load_dotenv()
# Enable debug mode.
DEBUG = True

# Connect to development database (SQLite)
SQLALCHEMY_DATABASE_URI = 'sqlite:///../../mbs.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Application Configuration
SECRET_KEY = os.getenv("SECRET_KEY")
ENVIRONMENT = os.getenv("ENVIRONMENT") == "DEV"
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))

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

