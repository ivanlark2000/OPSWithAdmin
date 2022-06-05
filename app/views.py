import math
from app import app, Flat
from flask import render_template, redirect, url_for, request
from flask_security import logout_user


@app.route('/')
def index():
    flats = Flat.query.limit(4).all()
    # делаем запрос к базе и получаем первые четыре квартиры
    pages = [i for i in range(1, (math.ceil(len(flats) / 4) + 1))]
    # определяем количество страниц
    print(request.url)
    return render_template('index.html', flats=flats, pages=pages)


@app.route('/<int:page>')
def other_pages(page):
    flats = Flat.query.all()
    pages = [i for i in range(1, (math.ceil(len(flats) / 4) + 1))]
    try:
        flats = flats[page * 4 - 4:page * 4]
    except:
        flats = flats[page * 4 - 4:]
    return render_template('index.html', flats=flats, pages=pages)


@app.route('/flat/<int:flat_id>/')
def flat(flat_id):
    flat = Flat.query.get(flat_id)
    return render_template('flat.html', flat=flat)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def not_found_error(error):
    return render_template('500.html'), 500
