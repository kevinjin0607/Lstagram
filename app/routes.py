# this file serves as a controller
from flask import render_template, flash, redirect, url_for
from app import appInstance
from app.forms import LoginForm


@appInstance.route('/')
@appInstance.route('/index')
def index():
    # mock data
    user = {'username': 'Lily'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


@appInstance.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # check if form submit action
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
