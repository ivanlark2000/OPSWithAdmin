from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
# @login_required
def index():
    return render_template('index.html', title='Home Page')


@app.route('/admin/')
# @login_required
def admin():
    return render_template('admin.html', title='Home')