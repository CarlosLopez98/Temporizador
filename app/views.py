from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, RegisterForm
from .models import User, Work
from . import login_manager


page = Blueprint('page', __name__)

@login_manager.user_loader
def load_user(id):
    return User.get_by_id(id)

@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title='Error 404'), 404


# ruta principal
@page.route('/')
def index():
    return render_template('index.html', title='Home')

@page.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    return render_template('auth/login.html', title='Login', form=form)
