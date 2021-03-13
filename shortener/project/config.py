import os
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    FLASK_ENV = environ.get("FLASK_ENV")
    SQL_HOST = environ.get("SQL_HOST")
    SQL_PORT = environ.get("SQL_PORT")
    DATABASE = environ.get("DATABASE")
    APP_FOLDER = environ.get("APP_FOLDER")
    SECRET_KEY = os.urandom(32)
