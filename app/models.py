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

    def __repr__(self):
        return f'Role - {self.name}'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), index=True, nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(500), index=True, nullable=False)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f'User - {self.username}'


class Flat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(64), index=True, nullable=False)
    price = db.Column(db.Integer(), index=True, nullable=False)
    district = db.Column(db.String(64), index=True, nullable=False)
    away_settlement = db.Column(db.Boolean(), index=True)
    numbers_of_room = db.Column(db.Integer(), index=True)
    type_of_room = db.Column(db.String(64))
    total_space = db.Column(db.Float(5), index=True)
    space_of_kitchen = db.Column(db.Float(5), index=True)
    space_of_living = db.Column(db.Float(5), index=True)
    furniture = db.Column(db.String(150))
    technics = db.Column(db.String(150))
    balcony_or_loggia = db.Column(db.String(150))
    ceiling_height = db.Column(db.Float(5), index=True)
    bathroom = db.Column(db.String(150))
    widow = db.Column(db.String(150))
    repair = db.Column(db.String(150))
    floor = db.Column(db.Integer(), index=True, nullable=False)
    description = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    image = db.relationship('Image', backref='image')
    # Аргумент backref определяет имя поля, которое будет добавлено к объектам класса «много»

    def __repr__(self):
        return f'Квартира по адресу {self.address}'


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))
    flat_id = db.Column(db.Integer, db.ForeignKey('flat.id'))

    def __repr__(self):
        return f'ImageFlat/{self.path}'





