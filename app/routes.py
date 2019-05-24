from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from main import ls, current_path


@app.route('/')
@app.route('/index')
def index():
    cwd = current_path()
    user = {'username': 'root'}
    listing = ls()

    return render_template('index.html', title='File Manager', user=user, items=listing, cwd=cwd)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
