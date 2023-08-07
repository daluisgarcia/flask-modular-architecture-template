from datetime import timedelta

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, abort, current_app
)
from flask_login import login_user, logout_user, login_required
from flask_principal import Identity, AnonymousIdentity, identity_changed

from sqlalchemy import exc
from core.utilities import is_safe_url
from core.auth.forms import LoginForm, RegisterForm
from core.auth import UserRepository


bp = Blueprint('auth', __name__, url_prefix='')


@bp.route('/register', methods=('GET', 'POST'))
def register():

    form = RegisterForm()

    if form.validate_on_submit():
        try:
            user_repo = UserRepository()
            username: str = form.username.data
            password: str = form.password.data
            user_repo.register_user(username, password)
        except exc.IntegrityError:
            flash(f"User {username} is already registered.")
        else:
            return redirect(url_for("auth.login"))

    return render_template('register.html', form=form)


@bp.route('/login', methods=('GET', 'POST'))
def login():

    form = LoginForm()

    if form.validate_on_submit():

        username: str = form.username.data
        password: str = form.password.data
        remember_me: bool = form.remember_me.data

        user_repo = UserRepository()
        user = user_repo.login_user(username, password)

        if user is None:
            flash('Incorrect credentials.')
        else:
            login_user(user, remember=remember_me, duration=timedelta(days=1))
            
            # Tell Flask-Principal the identity changed
            identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))

            next = request.args.get('next')

            if not is_safe_url(next):
                return abort(400)

            return redirect(next or url_for('blog.index'))

    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    # Tell Flask-Principal the user is anonymous
    identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())
    return redirect(url_for('main.index'))
