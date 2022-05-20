from app import app, db
from app.models import Admin, Flat


@app.shell_context_processor
#  регистрирует функцию как функцию контекста оболочки
def make_shell_context():
    return {'db': db, 'Admin': Admin, 'Flat': Flat}