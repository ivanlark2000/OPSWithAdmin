import os
import flask_admin
from flask import Flask, url_for, request, session
from flask_admin import helpers as admin_helpers
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore


from config import Config
from flask_babelex import Babel
path = os.path.join(os.path.dirname(__file__), 'static/ImageFlat')

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

# Create database connection object
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Setup Flask-Security
from app.models import User, Role, Flat, Image

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create admin
admin = flask_admin.Admin(app, 'Администрация', base_template='my_master.html',
                          template_mode='bootstrap4')

from app.adminView import MySuperUserModelView, MyAdminModelView, ImageModelView


admin.add_view(MySuperUserModelView(User, db.session, category='Team'))
admin.add_view(MySuperUserModelView(Role, db.session, category='Team'))
admin.add_sub_category(name='Команда', parent_name='Team')
admin.add_view(MyAdminModelView(Flat, db.session, name='Квартиры'))
admin.add_view(ImageModelView(Image, db.session, name='Фото'))


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )


@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'ru')


from app import views
