from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, ValidationError
from wtforms.validators import InputRequired, Email, Length, AnyOf
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyOne!'
bootstrap = Bootstrap(app)


class User:
    def __init__(self, username, password, entrydate):
        self.username = username
        self.password = password
        self.entrydate = entrydate


class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[InputRequired(), Email(message='I don\'t like your email')])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=10), AnyOf(['secret', 'password'])])
    entrydate = DateField('Entry Date', format="%Y-%m-%d")

    def validate_username(form, field):
        if field.data != 'cookie@gmail.com':
            raise ValidationError('You do not have the correct username!')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    user = User(username='Cookie', password='password', entrydate='2020-01-01')
    print(user.username)
    print(user.password)

    if form.validate_on_submit():
        form.populate_obj(user)
        print(user.username)
        print(user.password)
        print(user.entrydate)

        return 'Form sucessfully submitted'
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
