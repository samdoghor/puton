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

application_secret_key = env_var["secret_key"]

#  ai configuration

ai_api_key = env_var["ai_api_key"]
ai_model = env_var["ai_model"]

# databases

# local database

database_username = env_var["database_username"]
database_password = env_var["database_password"]
database_host = env_var["database_host"]
database_port = int(env_var["database_port"])
database_name = env_var["database_name"]

# production database

# database_username = env_var["production_database_user"]
# database_password = env_var["production_database_password"]
# database_host = env_var["production_database_host"]
# database_port = int(env_var["production_database_port"])
# database_name = env_var["production_database_name"]

database_uri = f"postgresql+psycopg://{database_username}:{database_password}@{database_host}:{database_port}/{database_name}"  # noqa

database_tracker = False

# application configurations

application_root = env_var["apiApplication_root"]
application_host = env_var["application_host"]
application_port = int(env_var["application_port"])
application_path = env_var["apiApplication_path"]

# application running environment

application_environment = env_var["environment"]
application_debug = True
