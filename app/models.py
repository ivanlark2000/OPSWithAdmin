from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login


@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_name = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Admin {}>'.format(self.admin_name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
         return check_password_hash(self.password_hash, password)