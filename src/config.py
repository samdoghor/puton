"""src/config.py

Keyword arguments:
argument -- None
Return: all configuration related to puton
"""

#  imports

import dotenv

#  environment variables configuration

env_var = dotenv.dotenv_values('.env')  # noqa - sets env file to load env variables

# security

application_secret_key = env_var["SECRET_KEY"]

#  ai configuration

ai_api_key = env_var["AI_API_KEY"]
ai_model = env_var["AI_MODEL"]

# database

database_username = env_var["DATABASE_USERNAME"]
database_password = env_var["DATABASE_PASSWORD"]
database_host = env_var["DATABASE_HOST"]
database_port = int(env_var["DATABASE_PORT"])
database_name = env_var["DATABASE_NAME"]

database_uri = f"postgresql+psycopg://{database_username}:{database_password}@{database_host}:{database_port}/{database_name}"  # noqa

database_tracker = False

# application configurations

application_root = env_var["APPLICATION_ROOT"]
application_host = env_var["APPLICATION_HOST"]
application_port = int(env_var["APPLICATION_PORT"])
application_path = env_var["APPLICATION_PATH"]

# application running environment

application_environment = env_var["ENVIRONMENT"]
application_debug = env_var["APPLICATION_DEBUG"]
