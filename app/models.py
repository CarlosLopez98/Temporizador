from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    encrypted_password = db.Column(db.String(94), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now())
    works = db.relationship('Work', lazy='dynamic')

    def verify_password(self, password):
        return check_password_hash(self.encrypted_password, password)

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value):
        self.encrypted_password = generate_password_hash(value)

    def __str__(self):
        return self.username

    @classmethod
    def create_element(cls, username, age, password, email):
        user = User(username=username, age=age, password=password, email=email)

        db.session.add(user)
        db.session.commit()

        return user

    @classmethod
    def get_by_id(cls, id):
        return User.query.filter_by(id=id).first()

    @classmethod
    def get_by_username(cls, username):
        return User.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return User.query.filter_by(email=email).first()


class Work(db.Model):
    __tablename__ = 'works'

    id = db.Column(db.Integer, primary_key=True)
    total_time = db.Column(db.Integer, nullable=False) #Tiempo total de la sesion
    total_work_time = db.Column(db.Integer, nullable=False) # Tiempo total que trabajo el cliente en segundos
    work_time = db.Column(db.Integer, nullable=False) # Tienmpo de trabajo por minuto
    rest_time = db.Column(db.Integer, nullable=False) # Tiempo de descanso por minuto
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime, default=datetime.datetime.now())

    @classmethod
    def create_element(cls, total_time, total_work_time, work_time, rest_time, user_id):
        work = Work(total_time=total_time, total_work_time=total_work_time, work_time=work_time, rest_time=rest_time, user_id=user_id)

        db.session.add(work)
        db.session.commit()

        return work

    @classmethod
    def get_by_id(cls, id):
        return Work.query.filter_by(id=id).first()
