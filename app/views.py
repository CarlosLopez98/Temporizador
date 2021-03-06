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
    if current_user.is_authenticated:
        return redirect(url_for('page.index'))

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        user = User.get_by_username(username)
        if user and user.verify_password(password):
            login_user(user)
            flash('Usuario autenticado.', 'success')

            return redirect(url_for('page.index'))

        else:
            flash('Username o password incorrectos.', 'danger')

    return render_template('auth/login.html', title='Login', form=form)

@page.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('page.index'))

    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        age = form.age.data
        email = form.email.data
        password = form.password.data

        user = User.create_element(username, age, password, email)
        flash('Usuario registrado con éxito.', 'success')

        return redirect(url_for('page.login'))

    return render_template('auth/signup.html', title='Signup', form=form)

@page.route('/logout')
def logout():
    logout_user()
    flash('Cerraste sesión exitosamente.', 'success')
    return redirect(url_for('page.index'))


# Views para el work
@page.route('/work/history/<int:id>')
@login_required
def work_history(id):
    if id == current_user.id:
        works = current_user.works

        return render_template('work/history.html', title='Tu historial', works=works)
    else:
        return redirect(url_for('page.work_history', id=current_user.id))

@page.route('/work/save', methods=['GET'])
@login_required
def save_work():
    if request.method == 'GET':
        tneto = request.args.get('tneto')
        tjob = request.args.get('tjob')
        texe = request.args.get('texe')
        trest = request.args.get('trest')

        if tneto and tjob and texe and trest:
            work = Work.create_element(tneto, tjob, texe, trest, current_user.id)

            flash('Se creó un registro de trabajo.', 'success')
        else:
            flash('Hubo un fallo al crear el registro de trabajo', 'danger')
            
        return redirect(url_for('page.index'))
    else:
        return redirect(url_for('page.index'))
