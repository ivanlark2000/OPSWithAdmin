from app import app
from flask import render_template, redirect, url_for
from flask_security import logout_user


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/les')
def les():
    return render_template('_flatcard.html')