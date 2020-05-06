from app import create_app
from app import db, User, Work
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from config import config


config_class = config['development']
app = create_app(config_class)


if __name__ == '__main__':
    manager = Manager(app)

    manager.run()
