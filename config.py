import os
from dotenv import load_dotenv

load_dotenv(override=True)
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = os.environ.get('PASSWORD_SALT')
    SECURITY_PASSWORD_HASH = os.environ.get('PASSWORD_HASH')
    FLASK_ADMIN_SWATCH = 'cyborg'