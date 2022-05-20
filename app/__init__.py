from flask import Flask
from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


from config import Config
from flask_login import LoginManager
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import Flat
admin = Admin(app, name='Roman-production', template_mode='bootstrap3')
admin.add_view(ModelView(Flat, db.session))

from app import view, models