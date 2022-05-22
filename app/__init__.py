import flask_admin
from flask import Flask, url_for

from flask_admin import helpers as admin_helpers

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, LoginForm
from config import Config

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

from app.adminView import MySuperUserModelView, MyAdminModelView
admin.add_view(MySuperUserModelView(User, db.session))
admin.add_view(MySuperUserModelView(Role, db.session))
admin.add_view(MyAdminModelView(Flat, db.session))


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )


from app import views
