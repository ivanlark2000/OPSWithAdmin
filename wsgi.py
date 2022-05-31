from app import app, db, user_datastore
from app.models import User, Flat, Role


@app.shell_context_processor
#  регистрирует функцию как функцию контекста оболочки
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Role': Role,
        'user_datastore': user_datastore,
        'Flat': Flat,
    }