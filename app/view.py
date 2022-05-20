from flask import render_template, url_for, flash, request
from flask_login import login_required, current_user, login_user
from werkzeug.urls import url_parse
from werkzeug.utils import redirect

from app import app
from app.forms import Authorization

from app.models import Admin


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@login_required
@app.route('/admin/')
@login_required
def admin():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        #  is_authenticated: свойство, которое имеет значение True, если пользователь имеет действительные
        #  учетные данные
        return redirect(url_for('admin'))
    form = Authorization()
    print('валидация прошла ', form.validate_on_submit())
    if form.validate_on_submit():
        user = Admin.query.filter_by(admin_name=form.admin_name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Не корректно введен пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.admin_name.data)
        # эта функция устанавливает переменную для зарегистрированного пользователя current user
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('admin')
        return redirect(next_page)
    return render_template('login.html', title='Авторизация', form=form)