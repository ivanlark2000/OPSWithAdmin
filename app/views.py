from app import app, Flat
from flask import render_template, redirect, url_for
from flask_security import logout_user


@app.route('/')
def home():
    flats = Flat.query.all()
    pages = [i for i in range(1,  (len(flats) // 4 + 1))]
    return render_template('index.html', flats=flats, pages=pages)


@app.route('/<int:page>')
def other_pages(page):
    flats = Flat.query.all()
    pages = [i for i in range(1, (len(flats) // 4 + 1))]
    try:
        flats = flats[page * 4 - 4:page * 4]
    except:
        flats = flats[page * 4 - 4:]
    return render_template('index.html', flats=flats, pages=pages)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/les')
def les():
    return render_template('_flatcard.html')