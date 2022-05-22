from flask import redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class MySuperUserModelView(ModelView):
    def is_accessible(self):
        return current_user.has_role('SuperUser')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class MyAdminModelView(ModelView):
    def is_accessible(self):
        return current_user.has_role('SuperUser') or current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))