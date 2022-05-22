from app import app
from flask import render_template, redirect, url_for
from flask_security import login_required, logout_user


@app.route('/')
@login_required
def home():
    return render_template('index.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))