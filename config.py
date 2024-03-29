import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


# class Config:
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
#     FLASK_DEBUG = 1


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    