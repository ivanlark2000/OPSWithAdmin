from app import app, db, user_datastore
from app.models import User, FotoFlat, Flat


@app.shell_context_processor
#  регистрирует функцию как функцию контекста оболочки
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'user_datastore': user_datastore,
        'Flat': Flat,
        'FotoFlat': FotoFlat
    }