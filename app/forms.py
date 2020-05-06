from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, HiddenField, TextAreaField
from wtforms.fields.html5 import EmailField

from .models import User


def lenght_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('Solo los humanos pueden completar este registro!')


class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message='El campo debe tener entre 4 y 50 caracteres.'),
    ])
    password = PasswordField('Password', [
        validators.Required(message='El email es requerido.'),
    ])

class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50)
    ])
    email = EmailField('Email', [
     validators.length(min=6, max=100, message='El campo debe tener entre 4 y 50 caracteres.'),
     validators.Required(message='El email es requerido.'),
     validators.Email(message='Ingrese un email válido.')
    ])
    password = PasswordField('Password', [
        validators.Required(message='El password es requerido.'),
        validators.EqualTo('confirm_password', message='La contraseña no coincide')
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField('Acepto términos y condiciones', [
        validators.DataRequired()
    ])
    honeypot = HiddenField('', [ lenght_honeypot])


    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('El username ya se encuentra registrado.')

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('El email ya se encuentra registrado.')

    # Sobreescritura del metodo validate
    def validate(self):
        if not Form.validate(self):
            return False

        # Validaciones propias
        if len(self.password.data) < 4:
            self.password.errors.append('El password es demasiado corto.')
            return False

        return True
