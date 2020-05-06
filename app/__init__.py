from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()


from .views import page
from .models import User, Work


def create_app(config):
    app.config.from_object(config)

    csrf.init_app(app)
    app.register_blueprint(page)

    login_manager.init_app(app)
    login_manager.login_view = 'page.login'
    login_manager.login_message = 'Es necesario iniciar sesión.'

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
