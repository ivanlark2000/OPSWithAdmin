import os
from dotenv import load_dotenv

load_dotenv(override=True)
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Data-Base
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_URL = '/static/'
    # Flask-Security
    SECURITY_PASSWORD_SALT = os.environ.get('PASSWORD_SALT')
    SECURITY_PASSWORD_HASH = os.environ.get('PASSWORD_HASH')
    FLASK_ADMIN_SWATCH = 'cyborg'
    # SECURITY_LOGIN_URL = '/admin'
    SECURITY_POST_LOGIN_VIEW = '/admin'