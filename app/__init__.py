import flask_admin
from flask import Flask, url_for

from flask_admin.contrib.sqla import ModelView

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, LoginForm
from config import Config
from flask_admin import helpers as admin_helpers


app = Flask(__name__)
app.config.from_object(Config)

# Create database connection object
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Setup Flask-Security
from app.models import User, Role, Flat

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create admin
admin = flask_admin.Admin(app, 'MyApp', base_template='my_master.html',
    template_mode='bootstrap3')


class MyModelView(ModelView):
    pass


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Flat, db.session))

# # Create a user to test with
# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='matt@nobien.net', password='password')
#     db.session.commit()


from app import views
