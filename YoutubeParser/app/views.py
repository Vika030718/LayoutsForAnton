"""Main views"""
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import SearchForm, RegistrationForm, LoginEmailForm
from .models import User, SearchHistory, ROLE_USER, ROLE_ADMIN
from .youtube_sercher import Searcher
import datetime

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/<int:page>', methods = ['GET', 'POST'])
def index():
    if g.user is None or g.user.is_authenticated == False:
        return redirect(url_for('login'))
    user = g.user
    form = SearchForm()
    if form.validate_on_submit():
        video = Searcher().youtube_search_all(form.search_field.data)
        p = SearchHistory(body=form.search_field.data, timestamp=datetime.datetime.utcnow(), author=user)
        db.session.add(p)
        db.session.commit()
        return render_template('index.html',
                               title='Home',
                               form=form,
                               user=user,
                               video=video,
                               video_count=len(video))
    return render_template('index.html',
                           title='Home',
                           form=form,
                           user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    user = g.user
    login_email_form = LoginEmailForm()
    if login_email_form.validate_on_submit():
        user = User.query.filter_by(email=login_email_form.login_email.data).first()
        password = user.password
        if user and login_email_form.login_password.data == password:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Email or password is incorrect.')
    return render_template('login.html',
                           title='Sign In',
                           login_email_form=login_email_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    nickname = form.email.data
    password = form.password.data
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first() is None:
            import ipdb
            ipdb.set_trace()
            user = User(nickname=nickname.split('@')[0], email=form.email.data, password=password, role=ROLE_USER)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash("You are already register on our site")
    return render_template('register.html',
                           title='Sign In',
                           form=form)

def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    login_user(user)
    return redirect(request.args.get('next') or url_for('index'))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    posts = SearchHistory.query.filter_by(user_id=user.id).all()
    if user is None:
        flash('User ' + nickname + ' not found.')
        return redirect(url_for('index'))
    return render_template('user.html',
                           user=user,
                           posts=posts)

