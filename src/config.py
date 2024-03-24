"""src/config.py

Keyword arguments:
argument -- None
Return: all configuration related to puton
"""

#  imports

import dotenv
from sqlalchemy import create_engine

#  environment variables configuration

env_var = dotenv.dotenv_values('.env')  # noqa - sets env file to load env variables

#  ai configuration

ai_api_key = env_var["ai_api_key"]
ai_model = env_var["ai_model"]


# databases

db = create_engine("sqlite+pysqlite:///:memory:", echo=True)  # noqa - test database
