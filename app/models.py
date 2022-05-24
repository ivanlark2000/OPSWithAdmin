from datetime import datetime
from flask_security import RoleMixin, UserMixin
from app import db


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '{}'.format(self.username)


class Flat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(64), index=True, nullable=False)
    price = db.Column(db.Integer(), index=True, nullable=False)
    district = db.Column(db.String(64), index=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    fotos = db.relationship('FotoFlat', backref='flat', lazy='dynamic')
    # Аргумент backref определяет имя поля, которое будет добавлено к объектам класса «много»

    def __repr__(self):
        return '<Flat {}>'.format(self.address)


class FotoFlat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url_pic = db.Column(db.String(200), nullable=False)
    pic = db.Column(db.LargeBinary, nullable=False)
    flat_id = db.Column(db.Integer, db.ForeignKey('flat.id'))

    def __repr__(self):
        return '{}'.format(self.url_pic)