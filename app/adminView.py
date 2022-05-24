from flask import redirect, request, url_for
from flask_admin import expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField, ImageUploadField, ImageUploadInput
from flask_login import current_user
from flask_security import url_for_security
from flask_admin.contrib import sqla


class MySuperUserModelView(ModelView):
    def is_accessible(self):
        return current_user.has_role('SuperUser')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for_security('login', next=request.url))


class MyAdminModelView(ModelView):
    def is_accessible(self):
        return current_user.has_role('SuperUser') or current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for_security('login', next=request.url))

    @expose('/new/', methods=['GET', 'POST'])
    def flat(self):
        return self.render('/home/ivan/Документы/PROJECT/OPS2/app/templates/admin/flat.html')


