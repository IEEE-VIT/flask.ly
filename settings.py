import os
from environs import Env


# environs loads environment variables from
# separate .env file from project root folder
# copy .env.template to .env and make changes if necessary
env = Env()
env.read_env()


# Project root dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Flask
DEBUG = env.bool("DEBUG", False)
SECRET_KEY = env.str("SECRET_KEY", "ssshhh")

# SQLAlchemy
SQLALCHEMY_DATABASE_NAME = env.str("SQLALCHEMY_DATABASE_NAME", "db.sqlite3")
SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/{SQLALCHEMY_DATABASE_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
