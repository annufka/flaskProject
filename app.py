from flask import Flask, flash, redirect, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from config import Config

app = Flask(__name__)
app.config.from_object(Config)


class HelloForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField('Привітатись')


@app.route('/form', methods=["GET", "POST"])
def hello_user():
    form = HelloForm()
    if form.validate_on_submit():
        flash('Привіт, {}'.format(form.email.data))
        result=form.email.data
    else:
        result="No info"
    return render_template('hello.html', title='Форма', form=form, result=result)


@app.route('/')
def home():  # put application's code here
    return 'Це початкова сторінка, якщо хочеш перейти до форми, то тицни <a href="/form">сюди</a>!'


if __name__ == '__main__':
    app.run()
